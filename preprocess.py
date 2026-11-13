#!/usr/bin/env python3
"""
Pre-processore semplice per file Markdown.
Legge un file riga per riga. Se trova '#include <file.md>', 
lo espande ricorsivamente. Altrimenti, stampa la riga.
"""

import sys
import os
import re

def process_file(filepath, visited=None):
    # Inizializza il set dei file visitati per evitare inclusioni circolari
    if visited is None:
        visited = set()
    
    # Risolvi il percorso assoluto per gestire correttamente i percorsi relativi
    abs_path = os.path.abspath(filepath)
    
    # Controllo dipendenze circolari
    if abs_path in visited:
        print(f"<!-- ERRORE: Inclusione circolare rilevata per '{filepath}' -->", file=sys.stderr)
        return
    
    visited.add(abs_path)
    
    # Controllo esistenza file
    if not os.path.isfile(abs_path):
        print(f"<!-- ERRORE: File non trovato '{filepath}' -->", file=sys.stderr)
        return

    # Leggi il file riga per riga
    in_code_block = False
    with open(abs_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Controlla se la linea inizia con <!--# (ignorando eventuali spazi iniziali)
            if line.lstrip().startswith("<!--#"):
                # Se il tag di chiusura non è sulla stessa riga, avanza fino a trovarlo
                while "#-->" not in line:
                    try:
                        line = next(f)
                    except StopIteration:
                        # Evita errori se il file termina prima di trovare #-->
                        break
                    # Salta al prossimo giro del ciclo 'for' senza elaborare la riga di chiusura
                    continue            # Non copiare i commenti tra <!--# e #-->
                
            # Rileva blocchi di codice Markdown (```)
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                print(line, end='')
                continue

            # Verifica se la riga inizia con #include <...> solo fuori dai blocchi di codice
            match = re.match(r'^\s*#include\s*<(.+?)>\s*$', line) if not in_code_block else None
            
            if match:
                # Estrai il nome del file (gruppo 1 della regex)
                include_file = match.group(1)
                
                # Risolvi il percorso relativo rispetto alla directory del file corrente
                current_dir = os.path.dirname(abs_path)
                target_path = os.path.join(current_dir, include_file)
                if not os.path.isfile(target_path) and os.path.isfile(target_path + '.md'):
                    target_path = target_path + '.md'
                
                # Chiamata ricorsiva
                process_file(target_path, visited)
            else:
                # Se non è un include, stampa la riga così com'è
                print(line, end='')

if __name__ == "__main__":
    # Se viene passato un argomento da riga di comando, usalo, altrimenti default a 'README.md' o 'index.md'
    target_file = sys.argv[1] if len(sys.argv) > 1 else 'index.md'
    process_file(target_file)
