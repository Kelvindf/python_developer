"""
#TODO - atividade: Crie um programa que faça as seguintes operações:
- Inserir dados de novo usuário
- Exibir lista de usuários
- Alterar dados de um usuário já cadastrado
- Excluir usuário da lista
- Sair do programa

Os dados a serem cadastrados serão os seguintes:
- Nome
- Data de nascimento
- E-mail
- CPF
- Telefone
- Profissão
- Gênero
# NOTE - a lista deve começar vazia
"""
import os

# Lista vazia para armazenar os usuários
usuarios = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("\n" + "="*50)
    print("MENU PRINCIPAL".center(50))
    print("="*50)
    print("1. Inserir novo usuário")
    print("2. Exibir lista de usuários")
    print("3. Alterar dados de um usuário")
    print("4. Excluir usuário")
    print("5. Sair do programa")
    print("="*50)

def inserir_usuario():
    limpar_tela()
    print("\n" + "="*50)
    print("CADASTRO DE NOVO USUÁRIO".center(50))
    print("="*50)
    
    usuario = {
        'Nome': input("Nome: "),
        'Data de nascimento': input("Data de nascimento (DD/MM/AAAA): "),
        'E-mail': input("E-mail: "),
        'CPF': input("CPF (somente números): "),
        'Telefone': input("Telefone: "),
        'Profissão': input("Profissão: "),
        'Gênero': input("Gênero: ")
    }
    
    usuarios.append(usuario)
    print("\nUsuário cadastrado com sucesso!")

def listar_usuarios():
    limpar_tela()
    print("\n" + "="*50)
    print("LISTA DE USUÁRIOS".center(50))
    print("="*50)
    
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    
    for i, usuario in enumerate(usuarios, 1):
        print(f"\nUSUÁRIO {i}:")
        for chave, valor in usuario.items():
            print(f"{chave}: {valor}")
        print("-"*50)

def alterar_usuario():
    limpar_tela()
    print("\n" + "="*50)
    print("ALTERAR DADOS DO USUÁRIO".center(50))
    print("="*50)
    
    if not usuarios:
        print("Nenhum usuário cadastrado para alterar.")
        return
    
    listar_usuarios()
    
    try:
        indice = int(input("\nDigite o número do usuário que deseja alterar: ")) - 1
        if indice < 0 or indice >= len(usuarios):
            print("Número de usuário inválido!")
            return
    except ValueError:
        print("Por favor, digite um número válido.")
        return
    
    usuario = usuarios[indice]
    print("\nDeixe em branco para manter o valor atual.")
    
    for chave in usuario:
        novo_valor = input(f"{chave} (atual: {usuario[chave]}): ")
        if novo_valor:
            usuario[chave] = novo_valor
    
    print("\nDados do usuário atualizados com sucesso!")

def excluir_usuario():
    limpar_tela()
    print("\n" + "="*50)
    print("EXCLUIR USUÁRIO".center(50))
    print("="*50)
    
    if not usuarios:
        print("Nenhum usuário cadastrado para excluir.")
        return
    
    listar_usuarios()
    
    try:
        indice = int(input("\nDigite o número do usuário que deseja excluir: ")) - 1
        if indice < 0 or indice >= len(usuarios):
            print("Número de usuário inválido!")
            return
    except ValueError:
        print("Por favor, digite um número válido.")
        return
    
    usuario_excluido = usuarios.pop(indice)
    print(f"\nUsuário {usuario_excluido['Nome']} excluído com sucesso!")

def main():
    while True:
        mostrar_menu()
        opcao = input("\nDigite a opção desejada: ")
        
        if opcao == '1':
            inserir_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            alterar_usuario()
        elif opcao == '4':
            excluir_usuario()
        elif opcao == '5':
            print("\nSaindo do programa...")
            break
        else:
            print("\nOpção inválida! Por favor, digite um número de 1 a 5.")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()