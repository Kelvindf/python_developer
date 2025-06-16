# Lista
import os

frutas = [
    "maçã",
    "banana",   
    "pera",
    "laranja",
    "uva",
    "abacaxi",
    "kiwi",
    "morango",
    "melancia"
]

# exibir a lista com seus respectivos índices
for i in range(len(frutas)):
    print(f"Indice {i}: {frutas[i]}.")

# O usuário informa o índice da fruta que deseja alterar
try:
    i = int(input("Informe o número do indice que deseja alterar: "))
    os.system("cls")  # Limpa o terminal
    if i >= 0 and i < len(frutas):
        print(f"Valor encontrado: {frutas[i]}")  
        frutas[i] = input("Informe o nome da nova fruta:")
    else:
        print("Indice inválido.")
except Exception as e:
    print(f"Não foi possível executar a operação: {e}")

finally:
    print("\nNova lista:\n")
    for i in range(len(frutas)):
        print(f"Indice {i}: {frutas[i]}.")    
  
