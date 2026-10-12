#!/usr/bin/env python3
# ==============================================================================
# Script: control_trazabilidad.py
# Proyecto: BioTrace-OSINT & Security Framework
# Autor: Alexis Isaac Solís Pinedo
# Descripción: Módulo de auditoría de trazabilidad, cadena de frío y bioseguridad
# ==============================================================================

import json
from datetime import datetime

# Limites biológicos y sanitarios (Temperatura en °C)
TEMP_MIN_OPTIMA = -18.0  # Para congelación
TEMP_MAX_OPTIMA = 4.0    # Para refrigeración fresca

def auditar_lote(id_lote, producto, temperatura, proveedor):
    """Evalúa la integridad de un lote según criterios de cadena de frío."""
    estado = "CONFORME"
    alerta = None
    
    if temperatura > TEMP_MAX_OPTIMA:
        estado = "CRÍTICO - RIESGO BACTERIOLÓGICO"
        alerta = f"Temperatura de {temperatura}°C excede el límite seguro de {TEMP_MAX_OPTIMA}°C."
    elif temperatura < TEMP_MIN_OPTIMA:
        estado = "DESVIACIÓN DE CONGELACIÓN"
        alerta = f"Temperatura de {temperatura}°C por debajo del rango estándar."

    registro = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "id_lote": id_lote,
        "producto": producto,
        "proveedor": proveedor,
        "temperatura_celsius": temperatura,
        "estado_bioseguridad": estado,
        "alerta": alerta
    }
    return registro

def main():
    print("====================================================")
    print("   BIOTRACE-OSINT: Control de Trazabilidad Bio    ")
    print("====================================================")
    
    # Simulación de auditoría de lotes de muestra
    lotes_auditar = [
        {"id": "LOTE-MAR-001", "producto": "Pulpo Falso / Tilapia", "temp": 2.5, "prov": "Distribuidora Central"},
        {"id": "LOTE-MAR-002", "producto": "Camarón Mediano", "temp": 7.8, "prov": "Mariscos del Pacífico"},
        {"id": "LOTE-MAR-003", "producto": "Filete Congelado", "temp": -20.1, "prov": "Congelados del Norte"}
    ]
    
    reportes = []
    print("\n[+] Procesando auditoría de insumos...\n")
    
    for lote in lotes_auditar:
        res = auditar_lote(lote["id"], lote["producto"], lote["temp"], lote["prov"])
        reportes.append(res)
        
        simbolo = "✔" if "CONFORME" in res["estado_bioseguridad"] else "✖"
        print(f"[{simbolo}] {res['id_lote']} | {res['producto']} | Temp: {res['temperatura_celsius']}°C -> {res['estado_bioseguridad']}")
        if res["alerta"]:
            print(f"    └── ALERTA: {res['alerta']}")

    # Guardar reporte JSON
    archivo_salida = "reporte_trazabilidad.json"
    with open(archivo_salida, "w", encoding="utf-8") as f:
        json.dump(reportes, f, indent=4, ensure_ascii=False)
        
    print(f"\n[✔] Reporte de trazabilidad guardado en: {archivo_salida}")

if __name__ == "__main__":
    main()
