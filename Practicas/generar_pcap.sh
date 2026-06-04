#!/usr/bin/env bash
# Genera el archivo PCAP de práctica de redes — UTU 2026
# Uso: ./generar_pcap.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/generar_pcap.py"

# Verificar que existe el script Python
if [[ ! -f "$PYTHON_SCRIPT" ]]; then
    echo "Error: no se encontró $PYTHON_SCRIPT" >&2
    exit 1
fi

# Verificar que Python 3 está disponible
if ! command -v python3 &>/dev/null; then
    echo "Error: python3 no está instalado o no está en el PATH" >&2
    exit 1
fi

echo "======================================"
echo " Generador de PCAP — Redes UTU 2026  "
echo "======================================"
echo ""

python3 "$PYTHON_SCRIPT"

echo ""
echo "Listo. Abre el archivo .pcap con Wireshark."
