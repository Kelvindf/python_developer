import os
# coloque as letras iniciais maiusculas
# Lista de nomes        
nome = [
    "fulano",
    "ciclano",
    "beltrano",
    "joão",
    "maria",
    "jose",
    "ana",
    "pedro",
    "luana",
    "carla",
    "roberto"
]
# exibir a lista original
for i in range(len(nome)):
    print(f"Indice {i}: {nome[i]}.")
# O usuário informa o índice do nome que deseja alterar
try:
    i = int(input("Informe o número do indice que deseja excluir: "))
    os.system("cls")  # Limpa o terminal
    if i >= 0 and i < len(nome):
        print(f"item a ser excluído: {nome[i]}")
        confirmar = input("Você tem certeza que deseja excluir esse item? (s/n): ").lower().strip()
        os.system("cls")
        match confirmar:
            case "s":
                item_excluido = nome[i]
                del (nome[i])
                print(f"Item {item_excluido} excluído com sucesso!")
            case "n":
                print(f"{nome} não foi excluído.")
            case _:
                print("Opção inválida.")
    else:
        print("Índice inválido.")            
except Exception as e:
    print(f"Não foi possível excluir esse item: {e}")
finally:
    print("\nNova lista:\n")
    for i in range(len(nome)):
        print(f"Indice {i}: {nome[i]}.")
