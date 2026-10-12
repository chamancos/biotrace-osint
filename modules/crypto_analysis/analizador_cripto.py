#!/usr/bin/env python3
# ==============================================================================
# Script: analizador_cripto.py
# Proyecto: BioTrace-OSINT & Security Framework
# Autor: Alexis Isaac Solís Pinedo
# Descripción: Módulo de análisis de frecuencia de texto y cifrado Atbash
# ==============================================================================

import sys
from collections import Counter

def cifrado_atbash(texto):
    """Aplica la sustitución simétrica Atbash (A<->Z, B<->Y, etc.)."""
    resultado = []
    for char in texto:
        if 'a' <= char <= 'z':
            resultado.append(chr(ord('z') - (ord(char) - ord('a'))))
        elif 'A' <= char <= 'Z':
            resultado.append(chr(ord('Z') - (ord(char) - ord('A'))))
        else:
            resultado.append(char)
    return "".join(resultado)

def analisis_frecuencia(texto):
    """Calcula la frecuencia de cada carácter en el texto proporcionado."""
    caracteres_limpios = [c.lower() for c in texto if c.isalpha()]
    conteo = Counter(caracteres_limpios)
    total = len(caracteres_limpios)
    
    print("\n--- ANÁLISIS DE FRECUENCIA ---")
    print(f"Total de letras analizadas: {total}")
    print("Letra | Conteo | Porcentaje")
    print("---------------------------")
    for char, count in conteo.most_common(10):
        porcentaje = (count / total) * 100 if total > 0 else 0
        print(f"  {char.upper()}   |   {count:2d}   |   {porcentaje:.2f}%")

def main():
    print("====================================================")
    print("   BIOTRACE-OSINT: Módulo Criptográfico & Atbash    ")
    print("====================================================")
    
    if len(sys.argv) > 1:
        texto_entrada = " ".join(sys.argv[1:])
    else:
        texto_entrada = input("\nIngrese el texto o mensaje a analizar: ")
        
    if not texto_entrada.strip():
        print("[!] No se ingresó ningún texto.")
        return

    # 1. Transformación Atbash
    texto_atbash = cifrado_atbash(texto_entrada)
    print(f"\n[+] Texto Original : {texto_entrada}")
    print(f"[+] Cifrado Atbash : {texto_atbash}")
    
    # 2. Análisis de Frecuencia
    analisis_frecuencia(texto_entrada)

if __name__ == "__main__":
    main()
