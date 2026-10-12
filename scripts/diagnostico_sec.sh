#!/usr/bin/env bash
# ==============================================================================
# Script: diagnostico_sec.sh
# Proyecto: BioTrace-OSINT & Security Framework
# Autor: Alexis Isaac Solís Pinedo
# Descripción: Módulo de auditoría local para análisis de red, integridad y entorno
# ==============================================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

LOG_DIR="../docs/logs"
LOG_FILE="$LOG_DIR/auditoria_$(date +%Y%m%d_%H%M%S).log"

mkdir -p "$LOG_DIR"

echo -e "${BLUE}====================================================${NC}"
echo -e "${BLUE}   BIOTRACE-OSINT: Módulo de Auditoría Local        ${NC}"
echo -e "${BLUE}====================================================${NC}"
echo -e "Iniciando diagnóstico: $(date)\n" | tee -a "$LOG_FILE"

# 1. Identificación del Sistema y Entorno
echo -e "${YELLOW}[1] Información del Sistema:${NC}" | tee -a "$LOG_FILE"
echo "Usuario actual: $(whoami)" | tee -a "$LOG_FILE"
echo "Host: $(hostname)" | tee -a "$LOG_FILE"
echo "Kernel / SO: $(uname -a)" | tee -a "$LOG_FILE"
echo -e "----------------------------------------------------" | tee -a "$LOG_FILE"

# 2. Diagnóstico de Red e Interfaces
echo -e "${YELLOW}[2] Interfaces y Conectividad de Red:${NC}" | tee -a "$LOG_FILE"
if command -v ip >/dev/null 2>&1; then
    ip -4 addr show | grep -E 'inet' | tee -a "$LOG_FILE"
elif command -v ifconfig >/dev/null 2>&1; then
    ifconfig | grep -E 'inet' | tee -a "$LOG_FILE"
else
    echo -e "${RED}[!] No se encontraron herramientas de red (ip/ifconfig).${NC}" | tee -a "$LOG_FILE"
fi
echo -e "----------------------------------------------------" | tee -a "$LOG_FILE"

# 3. Verificación de Sockets y Conexiones Activas
echo -e "${YELLOW}[3] Conexiones Activas / Puertos Abiertos:${NC}" | tee -a "$LOG_FILE"
if command -v ss >/dev/null 2>&1; then
    ss -tulpn 2>/dev/null | tee -a "$LOG_FILE"
elif command -v netstat >/dev/null 2>&1; then
    netstat -tulpn 2>/dev/null | tee -a "$LOG_FILE"
else
    echo -e "${RED}[!] 'ss' o 'netstat' no disponibles en este entorno.${NC}" | tee -a "$LOG_FILE"
fi
echo -e "----------------------------------------------------" | tee -a "$LOG_FILE"

# 4. Estado del Almacenamiento
echo -e "${YELLOW}[4] Estado de Almacenamiento:${NC}" | tee -a "$LOG_FILE"
df -h . | tee -a "$LOG_FILE"
echo -e "----------------------------------------------------" | tee -a "$LOG_FILE"

echo -e "${GREEN}[✔] Auditoría completada con éxito.${NC}"
echo -e "Reporte guardado en: ${BLUE}$LOG_FILE${NC}"
