import { readdir, readFile, writeFile, rename } from "node:fs/promises";

const endCh = 30;
const beginCh = 7;

// Imposta su false per applicare davvero le modifiche
const DRY_RUN = false;
const TARGET_DIR = ".";

function pad(n: number): string {
  if (n > 9) {
    return "" + n;
  } else {
    return "0" + n;
  }
}

const entries = await readdir(TARGET_DIR, { withFileTypes: true });

let fileNames = [];
for (const entry of entries) {
  if (!entry.isFile()) continue;
  const NN = parseInt(entry.name.substr(0, 2));
  if (isNaN(NN) || NN > endCh || NN < beginCh) continue;
  const newNN = pad(NN + 1);
  const newOrder = NN + 1;
  const lastPart = entry.name.substr(2);
  const newFileName = newNN + lastPart;
  console.log(newFileName);
  const content = await readFile(entry.name, "utf8");
  const orderRegex = /^(order:\s*"?)\d+("?\s*)$/gm;

  if (!orderRegex.test(content)) {
    console.warn(
      `Attenzione: nessuna riga "order: NN" trovata in '${entry.name}'`,
    );
  }
  const updatedContent = content.replace(
    /^(order:\s*"?)\d+("?\s*)$/gm,
    `$1${newOrder}$2`
  );

  if (DRY_RUN) {
    console.log(`[DRY-RUN] '${entry.name}' -> '${newFileName}' (order: ${newOrder})`);
  } else {
    await writeFile(entry.name, updatedContent, "utf8");
    await rename(entry.name, newFileName);
    console.log(`Aggiornato e rinominato: '${entry.name}' -> '${newFileName}'`);
  }
}
