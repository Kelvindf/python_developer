"""
#TODO - atividade: Crie um programa com um dicionário chamado 'usuario',com o seguinte menu:
- Cadastrar nova chave
- Exibir dados do usuário
- Alterar valor da chave
- Excluir chave
- Sair do programa

# NOTE - os dados a serem  enseridos precisam ter haver com os dados do usuário
"""

usuario = {}

def cadastrar_chave():
    chave = input("\nDigite o nome da nova chave: ").strip().lower()
    if chave in usuario:
        print(" Essa chave já existe!")
    else:
        valor = input(f"Digite o valor para '{chave}': ")
        usuario[chave] = valor
        print(f" '{chave}' cadastrado com sucesso!")

def exibir_dados():
    if not usuario:
        print("\n Nenhum dado cadastrado ainda.")
    else:
        print("\n--- Dados do Usuário ---")
        for chave, valor in usuario.items():
            print(f"{chave}: {valor}")

def alterar_valor():
    exibir_dados()
    if usuario:
        chave = input("\nQual chave deseja alterar? ").strip().lower()
        if chave in usuario:
            novo_valor = input(f"Digite o novo valor para '{chave}': ")
            usuario[chave] = novo_valor
            print(f" '{chave}' atualizado para '{novo_valor}'!")
        else:
            print(" Chave não encontrada.")

def excluir_chave():
    exibir_dados()
    if usuario:
        chave = input("\nQual chave deseja excluir? ").strip().lower()
        if chave in usuario:
            confirmacao = input(f"Tem certeza que deseja excluir '{chave}'? (s/n): ").strip().lower()
            if confirmacao == 's':
                del usuario[chave]
                print(f" '{chave}' removido!")
        else:
            print(" Chave não encontrada.")

while True:
    print("1 - Cadastrar nova chave")
    print("2 - Exibir dados do usuário")
    print("3 - Alterar valor da chave")
    print("4 - Excluir chave")
    print("5 - Sair do programa")
    opcao = input("\nEscolha uma opção (1/2/3/4/5): ").strip()

    if opcao == '1':
        cadastrar_chave()
    elif opcao == '2':
        exibir_dados()
    elif opcao == '3':
        alterar_valor()
    elif opcao == '4':
        excluir_chave()
    elif opcao == '5':
        print("\nPrograma encerrado. Até mais! ")
        break
    else:
        print(" Opção inválida. Digite um número de 1 a 5.")