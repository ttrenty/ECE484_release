#!/usr/bin/env bash
set -euo pipefail

# Clear the visible terminal + scrollback so your banner is the first thing
clear && printf '\033[3J'

# Ensure pixi is reachable even if shell init files weren't parsed
export PATH="${HOME}/.pixi/bin:/usr/local/bin:${PATH}"

if command -v pixi >/dev/null 2>&1; then
  PIXI_STATUS="✅ pixi is available"
else
  PIXI_STATUS="⚠️  pixi not found on PATH (try reopening the terminal)"
fi

cat <<'EOF'

╔══════════════════════════════════════════════════════════════╗
║  👋 Welcome to Assignment 1                                  ║
║                                                              ║
║  Your dependencies are pre-installed with pixi.              ║
║                                                              ║
║  ▶ Quick start:                                              ║
║    pixi run python -V                                        ║
║    pixi run tests                                            ║
╚══════════════════════════════════════════════════════════════╝
EOF

echo "Status: ${PIXI_STATUS}"

echo "You won't be able to read the PDF in here, open it from the GitHub repository page instead. Make sure to open all 7 pages!"

echo
