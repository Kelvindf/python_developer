"""
Crie um programa que receba o nome, o peso e a altura do usuário, e informe seu IMC (Índice de Massa Corporal) e informe seu diagnóstico de acordo com o valor de seu IMC:
- Magro demais
- Peso normal
- Acima do peso
- Obeso
- Obesidade nível II
- Obesidade mórbida
"""

try:
    nome = input("Informe seu nome: ")
    peso = float(input("Informe seu peso em kg: ").replace(",", "."))
    altura = float(input("Informe sua altura em m: ").replace(",", "."))
    imc = peso / altura**2

    print(f"IMC de {nome} é: {imc:,.2f}.")

    if imc <= 18.5:
        print(f"{nome} está abaixo do peso.")
    elif imc <= 25:
        print(f"{nome} está no seu peso ideal.")
    elif imc <= 30:
        print(f"{nome} está acima do peso.")
    elif imc <= 35:
        print(f"{nome} está obeso.")
    elif imc <= 40:
        print(f"{nome} está com obesidade nível II.")
    else:
        print(f"{nome} está com obesidade mórbida.")
except Exception as e:
    print(f"Não foi possível calcular o IMC. {e}.")