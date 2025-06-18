"""
# TODO - ATIVIDADE: Crie um programa onde o usuário possa fazer as seguintes operações:
- Calcular área de um quadrado
- Calcular área de um retângulo
- Calcular área de um triângulo
- Calcular área de um trapézio
- Sair do programa
# NOTE - O usuário deverá escolher a opearação em um menu
# NOTE - O programa deverá ser feito com funções
"""
import os
import math

def area_quadrado():
    lado = float(input("Digite o comprimento do lado do quadrado: "))
    return lado * lado

def area_retangulo():
    base = float(input("Digite o comprimento da base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    return base * altura

def area_triangulo():
    base = float(input("Digite o comprimento da base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    return (base * altura) / 2

def area_trapezio():
    base_maior = float(input("Digite o comprimento da base maior do trapézio: "))
    base_menor = float(input("Digite o comprimento da base menor do trapézio: "))
    altura = float(input("Digite a altura do trapézio: "))
    return ((base_maior + base_menor) * altura) / 2

# algoritmo principal
while True:
    print("\nMenu de Opções:")
    print("1 - Calcular área do quadrado")
    print("2 - Calcular área do retângulo")
    print("3 - Calcular área do triângulo")
    print("4 - Calcular área do trapézio")
    print("5 - Sair do programa")
    
    opcao = input("Informe a opção desejada: ").strip()
    
    os.system("cls" if os.name == "nt" else "clear")
    
    if opcao == "1":
        resultado = area_quadrado()
        print(f"A área do quadrado é: {resultado:.2f}")
    elif opcao == "2":
        resultado = area_retangulo()
        print(f"A área do retângulo é: {resultado:.2f}")
    elif opcao == "3":
        resultado = area_triangulo()
        print(f"A área do triângulo é: {resultado:.2f}")
    elif opcao == "4":
        resultado = area_trapezio()
        print(f"A área do trapézio é: {resultado:.2f}")
    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")
    
    input("Pressione Enter para continuar...")
    os.system("cls" if os.name == "nt" else "clear")