import { readdir, readFile, writeFile } from "node:fs/promises";
import { join } from "node:path";
import { $ } from "bun";

const endCh = 37;
const beginCh = 16;

// Imposta su false per applicare davvero le modifiche
const DRY_RUN = false;
const TARGET_DIR = ".";

function pad(n: number): string {
  return n > 9 ? "" + n : "0" + n;
}

const entries = await readdir(TARGET_DIR, { withFileTypes: true });

for (const entry of entries) {
  if (!entry.isFile()) continue;

  const NN = parseInt(entry.name.slice(0, 2), 10);
  if (isNaN(NN) || NN > endCh || NN < beginCh) continue;

  const newNN = pad(NN + 1);
  const newOrder = NN + 1;
  const lastPart = entry.name.slice(2);
  const newFileName = newNN + lastPart;

  const oldPath = join(TARGET_DIR, entry.name);
  const newPath = join(TARGET_DIR, newFileName);

  const content = await readFile(oldPath, "utf8");
  const orderRegex = /^(order:\s*"?)\d+("?\s*)$/gm;

  if (!orderRegex.test(content)) {
    console.warn(
      `Attenzione: nessuna riga "order: NN" trovata in '${entry.name}'`,
    );
  }

  const updatedContent = content.replace(
    /^(order:\s*"?)\d+("?\s*)$/gm,
    `$1${newOrder}$2`,
  );

  if (DRY_RUN) {
    console.log(`[DRY-RUN] git mv '${oldPath}' '${newPath}' (order: ${newOrder})`);
  } else {
    await writeFile(oldPath, updatedContent, "utf8");
    await $`git mv ${oldPath} ${newPath}`;
    console.log(`Aggiornato e rinominato con git mv: '${entry.name}' -> '${newFileName}'`);
  }
}
