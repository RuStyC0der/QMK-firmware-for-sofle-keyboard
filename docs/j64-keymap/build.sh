#!/usr/bin/env bash
# Regenerates the j64 keymap images from keymap.c. Needs python3 and Google Chrome (macOS path below).
set -euo pipefail
cd "$(dirname "$0")"
KEYMAP=../../keyboards/rustyc0der/sofle/choc/keymaps/j64/keymap.c
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
HERE="$PWD"

# screen version (dark)
python3 -I render.py "$KEYMAP" j64-keymap.svg
"$CHROME" --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=1.5 \
  --window-size=888,1518 --screenshot="$HERE/j64-keymap.png" "file://$HERE/j64-keymap.svg"

# print version (A4 landscape, light)
python3 -I render_print.py "$KEYMAP" j64-keymap-print.svg
"$CHROME" --headless --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
  --window-size=1754,1240 --screenshot="$HERE/j64-keymap-print.png" "file://$HERE/j64-keymap-print.svg"
TMP="$(mktemp -d)"
{ printf '<!doctype html><meta charset="utf-8"><style>@page{size:A4 landscape;margin:0}html,body{margin:0;background:#fff}svg{display:block;width:297mm;height:210mm}</style>\n'; cat j64-keymap-print.svg; } > "$TMP/print.html"
"$CHROME" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="$HERE/j64-keymap-print.pdf" "file://$TMP/print.html"
rm -rf "$TMP"
