#!/bin/bash
# Usage: ./build.sh 1   -> builds "Unit-1 Consolidated Notes.pdf" from source/unit1.html using headless Edge
cd "$(dirname "$0")"
EDGE="/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
HTML="$(cygpath -w "$PWD/unit$1.html")"
OUT="$(cygpath -w "$PWD/../Unit-$1 Consolidated Notes.pdf")"
"$EDGE" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="$OUT" "file:///${HTML//\//}"
