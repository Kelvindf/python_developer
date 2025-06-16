# um programa aonde o usuário cria uma lista de compras
# Declaração de variáveis


carrinho = []

while True:
    item = input("Informe o item: ").capitalize().strip()
    carrinho.append(item)
    print(f"{item} adicionado ao carrinho.")
    confirmar = input("Deseja adicionar mais itens? (s/n): ").strip().lower()
    match confirmar:
        case "s":
            continue
        case "n":
            break
        case _:
            print("Opção inválida. Encerrando o programa.")
            continue

# Ordenar a lista em ordem alfabética
carrinho.sort()

# Exibição de dados 
for item in carrinho:
    print(item)

 