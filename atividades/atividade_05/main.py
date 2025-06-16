"""
# TODO - atividade: Crie um programa que receba do usuário os seguintes dados:
- Nome
- CPF
- Data de Nascimento
- E-mail
- Gênero
- Telefone
- Endereço
- Altura em metros
- Peso em kg
- Tipo Sanguíneo
Ao final, o programa exibe esses dados.
# NOTE - deve ser feito utilizando o conceito de dicionário.
"""


import os

pessoa = {}

try:
    pessoa['nome'] = input("Informe o nome: ")
    pessoa['cpf'] = input("Informe o CPF: ")
    pessoa['data de nascimento'] = input("Informe a data de nascimento: ")
    pessoa['e-mail'] = input("Informe o e-mail: ")
    pessoa['gênero'] = input("Informe o gênero: ")
    pessoa['telefone'] = input("Informe o telefone: ")
    pessoa['endereço'] = input("Informe o endereço: ")
    pessoa['altura'] = float(input("Informe a altura: ").replace(",", "."))
    pessoa['peso'] = float(input("Informe o peso: ").replace(",", "."))
    pessoa['tipo sanguíneo'] = input("Informe o tipo sanguíneo: ")

    os.system("cls")

    for chave in pessoa: # type: ignore
        print(f"{chave.title()}: {pessoa.get(chave)}") # type: ignore
except Exception as e:
    print(f"Não foi possível rodar programa. {e}.")