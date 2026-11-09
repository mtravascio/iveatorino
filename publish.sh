#!/usr/bin/env bash
# Rigenera le pagine, committa e pubblica su GitHub Pages.
#
# Uso:  ./publish.sh "descrizione della modifica"
#       ./publish.sh            (messaggio automatico con la data)
set -euo pipefail
cd "$(dirname "$0")"

msg="${1:-Aggiornamento sito $(date +%d/%m/%Y)}"

python3 build.py

git add -A
if git diff --cached --quiet; then
  echo "Nessuna modifica da pubblicare."
  exit 0
fi

git commit -m "$msg"
git push

echo
echo "Pubblicato: $msg"
echo "GitHub Pages impiega 20-40 secondi. Controllo: Settings > Pages sul repository."
