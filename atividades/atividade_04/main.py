# importa biblioteca
import os

# lista
nomes = []

while True:
    print(f"{'-'*30} MENU {'-'*30}")
    print("1 - Inserir novo nome na lista")
    print("2 - Exibir lista")
    print("3 - Pesquisar nome na lista")
    print("4 - Alterar nome na lista")
    print("5 - Excluir nome na lista")
    print("6 - Sair do programa")

    opcao = input("Opção desejada: ").strip()

    os.system("cls")
    match opcao:
        case "1":
            novo_nome = input("Informe o nome a ser cadastrado: ").strip().title()
            os.system("cls")
            try:
                nomes.append(novo_nome) # type: ignore
                print(f"{novo_nome} inserido com sucesso.")
            except Exception as e:
                print(f"Não foi possível inserir nome na lista. {e}.")
            finally:
                continue
        case "2":
            print("\nLista:\n")
            try:
                for i in range(len(nomes)): # type: ignore
                    print(f"Índice {i}: {nomes[i]}.")
                print("\n")
            except Exception as e:
                print(f"Não foi possível exibir a lista. {e}.")
            finally:
                continue
        case "3":
            nome_pesquisado = input("Informe o nome a pesquisar: ").title().strip()
            os.system("cls")
            result = nomes.count(nome_pesquisado) # type: ignore
            print(f"{nome_pesquisado} foi encontrado {result} vezes.")
            continue
        case "4":
            try:
                i = int(input("Informe o índice que deseja alterar: "))
                if i >= 0 and i < len(nomes): # type: ignore
                    nomes[i] = input("Informe o novo nome: ")
                    print("Nome alterado com sucesso.")
                else:
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível alterar item da lista. {e}.")
            finally:
                continue
        case "5":
            try:
                i = int(input("Informe o índice que deseja excluir: "))
                if i >= 0 and i < len(nomes): # type: ignore
                    del(nomes[i])
                    print("Nome excluído com sucesso.")
                else:
                    print("Índice inválido.")
            except Exception as e:
                print(f"Não foi possível excluir nome. {e}.")
            finally:
                continue
        case "6":
            print("Programa encerrado! =D ")
            break
        case _:
            print("Opção inválida.")
            continue