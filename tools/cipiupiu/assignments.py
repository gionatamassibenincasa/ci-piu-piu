"""Creazione e aggiornamento dei repository template per Classroom50."""

from __future__ import annotations

import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

from . import core


@dataclass(frozen=True)
class AssignmentOptions:
    org: str
    classroom: str
    template_repo_name: str
    assignment_name: str
    assignment_slug: str
    deadline: str | None


def _assignment_slug(activity_id: str) -> str:
    """Rimuove il suffisso numerico usato per versionare le attività."""
    stem, separator, suffix = activity_id.rpartition("-")
    return stem if separator and suffix.isdigit() else activity_id


def _load_config(path: Path | None, activity_id: str) -> dict[str, Any]:
    if path is None:
        return {}
    if not path.is_file():
        raise ValueError(f"Configurazione non trovata: {path}")
    data = core.yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Configurazione non valida: {path}")
    assignments = data.get("assignments") or []
    if not isinstance(assignments, list):
        raise ValueError("Configurazione non valida: 'assignments' deve essere una lista")
    for assignment in assignments:
        if isinstance(assignment, dict) and assignment.get("activity_id") == activity_id:
            return {**data, "_assignment": assignment}
    raise ValueError(f"Activity non trovata nella configurazione: {activity_id}")


def resolve_options(
    chapter: core.Chapter,
    *,
    config_path: Path | None,
    org: str | None,
    classroom: str | None,
) -> AssignmentOptions:
    """Combina config di classe, argomenti CLI e metadati del capitolo."""
    config = _load_config(config_path, chapter.activity_id)
    classroom_config = config.get("classroom") or {}
    assignment = config.get("_assignment") or {}
    if not isinstance(classroom_config, dict) or not isinstance(assignment, dict):
        raise ValueError("Configurazione classroom o assignment non valida")

    resolved_org = org or classroom_config.get("org")
    resolved_classroom = classroom or classroom_config.get("classroom_name")
    if not resolved_org or not resolved_classroom:
        raise ValueError(
            "Specifica --org e --classroom oppure fornisci classroom.org e "
            "classroom.classroom_name nella configurazione"
        )

    repo_name = assignment.get("template_repo_name") or f"cpp-{chapter.activity_id}-template"
    if "/" in str(repo_name):
        raise ValueError("template_repo_name deve essere solo il nome del repository")

    return AssignmentOptions(
        org=str(resolved_org),
        classroom=str(resolved_classroom),
        template_repo_name=str(repo_name),
        assignment_name=str(assignment.get("title") or chapter.title),
        assignment_slug=str(assignment.get("slug") or _assignment_slug(chapter.activity_id)),
        deadline=str(assignment["deadline"]) if assignment.get("deadline") else None,
    )


def load_activity(activity_id: str, chapters_dir: Path | None = None) -> core.Chapter:
    """Trova un capitolo per activity_id e richiede almeno un file create."""
    for chapter in core.iter_chapters(chapters_dir):
        if chapter.activity_id != activity_id:
            continue
        if not any(
            isinstance(item, dict) and item.get("action") == "create"
            for item in chapter.meta.get("files") or []
        ):
            raise ValueError(f"{activity_id}: nessun files[].action=create")
        return chapter
    raise ValueError(f"Activity non trovata: {activity_id}")


def _destination(root: Path, relative_path: str) -> Path:
    path = PurePosixPath(relative_path)
    if path.is_absolute() or ".." in path.parts or path == PurePosixPath("."):
        raise ValueError(f"Percorso file non sicuro: {relative_path}")
    return root.joinpath(*path.parts)


def write_template_files(chapter: core.Chapter, destination: Path) -> None:
    """Materializza esclusivamente i file del frontmatter con action=create."""
    for item in chapter.meta.get("files") or []:
        if not isinstance(item, dict) or item.get("action") != "create":
            continue
        target = _destination(destination, str(item["path"]))
        target.parent.mkdir(parents=True, exist_ok=True)
        if "template_content" in item:
            content = str(item["template_content"])
        else:
            source = (core.ROOT / str(item["template_from"])).resolve()
            if core.ROOT not in source.parents or not source.is_file():
                raise ValueError(f"template_from non trovato o non sicuro: {item['template_from']}")
            content = source.read_text(encoding="utf-8")
        target.write_text(content, encoding="utf-8")


def _run(command: list[str], *, cwd: Path | None = None) -> str:
    result = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip() or "errore senza dettagli"
        raise RuntimeError(f"Comando fallito ({' '.join(command)}): {detail}")
    return result.stdout.strip()


def _repo_exists(repo: str) -> bool:
    result = subprocess.run(
        ["gh", "api", f"repos/{repo}"],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode == 0:
        return True
    if "http 404" in result.stderr.lower() or "not found" in result.stderr.lower():
        return False
    detail = result.stderr.strip() or result.stdout.strip() or "errore senza dettagli"
    raise RuntimeError(f"Impossibile verificare il repository {repo}: {detail}")


def _commit_and_push(repository_dir: Path, repo: str) -> None:
    _run(["git", "add", "--all"], cwd=repository_dir)
    status = _run(["git", "status", "--porcelain"], cwd=repository_dir)
    if not status:
        return
    _run(
        [
            "git",
            "-c",
            "user.name=ci-piu-piu",
            "-c",
            "user.email=ci-piu-piu@users.noreply.github.com",
            "commit",
            "-m",
            "Aggiorna scaffold attività",
        ],
        cwd=repository_dir,
    )
    _run(["git", "push", "origin", "HEAD"], cwd=repository_dir)


def publish_template(chapter: core.Chapter, options: AssignmentOptions) -> str:
    """Crea o aggiorna il template GitHub e ne abilita la modalità template."""
    repo = f"{options.org}/{options.template_repo_name}"
    with tempfile.TemporaryDirectory(prefix="cipiupiu-assignment-") as temp_dir:
        worktree = Path(temp_dir) / "repository"
        if _repo_exists(repo):
            _run(["git", "clone", "--quiet", f"https://github.com/{repo}.git", str(worktree)])
        else:
            _run(["gh", "repo", "create", repo, "--private"])
            worktree.mkdir()
            _run(["git", "init", "--initial-branch=main"], cwd=worktree)
            _run(["git", "remote", "add", "origin", f"https://github.com/{repo}.git"], cwd=worktree)

        write_template_files(chapter, worktree)
        _commit_and_push(worktree, repo)

    _run(["gh", "api", "--method", "PATCH", f"repos/{repo}", "-f", "is_template=true"])
    return f"https://github.com/{repo}"

