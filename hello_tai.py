#!/usr/bin/env python3
"""
hello_tai.py
Arquivo atualizado por Taiane para exercício de GitHub CLI
Versão: 2.0
Data: Março 2025
"""

import sys
from datetime import datetime

def saudacao(nome="Taiane"):
    """Retorna uma saudação personalizada."""
    hora_atual = datetime.now().hour
    
    if 5 <= hora_atual < 12:
        periodo = "Bom dia"
    elif 12 <= hora_atual < 18:
        periodo = "Boa tarde"
    else:
        periodo = "Boa noite"
    
    return f"{periodo}, {nome}! Bem-vinda ao exercício de GitHub CLI."

def calcular_soma(a, b):
    """Calcula a soma de dois números."""
    return a + b

def main():
    """Função principal do programa."""
    print("=" * 50)
    print("Sistema de Saudação - GitHub CLI Exercise")
    print("=" * 50)
    
    # Saudação personalizada
    mensagem = saudacao()
    print(f"\n{mensagem}")
    
    # Exemplo de cálculo
    resultado = calcular_soma(10, 20)
    print(f"\nExemplo de cálculo: 10 + 20 = {resultado}")
    
    # Informações do sistema
    print(f"\nPython version: {sys.version}")
    print(f"Data/hora atual: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    
    print("\n" + "=" * 50)
    print("Arquivo criado como parte do fluxo GitHub CLI")
    print("Branch: feat-update-hello-tai")
    print("=" * 50)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())