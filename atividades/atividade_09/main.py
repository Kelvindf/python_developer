"""
# TODO - atividade: Crie um programa que receba os dados de dois objetos diferentes da mesma classe Pessoa. 
Os dados serão os seguintes:
- Nome
- Idade
- E-mail
- Telefone
- Gênero
- tipo sanguíneo


suponha que o objeto 'usuario_2' esteja precisando de doação de sangue do 'usuario_1' . O programa deve informar os dados dos dois usuários, e ao do 'usuario_1'. O programa deve informar os dados dos dois usuários, e ao final, informar se o usuario_1 pode doar sangue para o usuario_2 ou não.
#NOTE - A última pergunta deverá ter uma resposta randômica.
"""


import random

class Pessoa:
    def __init__(self, nome, idade, email, telefone, genero, tipo_sanguineo):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.genero = genero
        self.tipo_sanguineo = tipo_sanguineo

    def mostrar_dados(self):
        print(f"\nDados de {self.nome}:")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Gênero: {self.genero}")
        print(f"Tipo sanguíneo: {self.tipo_sanguineo}")

def pode_doar_sangue(doador, receptor):
    # Compatibilidade básica de tipos sanguíneos
    compatibilidade = {
        'A+': ['A+', 'AB+'],
        'A-': ['A+', 'A-', 'AB+', 'AB-'],
        'B+': ['B+', 'AB+'],
        'B-': ['B+', 'B-', 'AB+', 'AB-'],
        'AB+': ['AB+'],
        'AB-': ['AB+', 'AB-'],
        'O+': ['A+', 'B+', 'AB+', 'O+'],
        'O-': ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    }
    
    # Verifica se o tipo do doador é compatível com o do receptor
    if receptor.tipo_sanguineo in compatibilidade.get(doador.tipo_sanguineo, []):
        # Retorna aleatoriamente True ou False (como mencionado no requisito)
        return random.choice([True, False])
    return False

if __name__ == "__main__":
    print("Cadastro do Usuário 1 (doador potencial):")
    usuario1 = Pessoa(
        input("Nome: ").title().strip(),
        input("Idade: "),
        input("E-mail: ").lower().strip(),
        input("Telefone: "),
        input("Gênero: ").strip(),
        input("Tipo sanguíneo (ex: A+, B-, O+): ").upper()
    )

    print("\nCadastro do Usuário 2 (receptor potencial):")
    usuario2 = Pessoa(
        input("Nome: ").title().strip(),
        input("Idade: "),
        input("E-mail: ").lower().strip(),
        input("Telefone: "),
        input("Gênero: ").strip(),
        input("Tipo sanguíneo (ex: A+, B-, O+): ").upper()
    )

    # Mostrar dados dos usuários
    usuario1.mostrar_dados()
    usuario2.mostrar_dados()

    # Verificar compatibilidade
    resultado = pode_doar_sangue(usuario1, usuario2)
    
    print("\nResultado da compatibilidade:")
    if resultado:
        print(f"{usuario1.nome} PODE doar sangue para {usuario2.nome}!")
    else:
        print(f"{usuario1.nome} NÃO PODE doar sangue para {usuario2.nome}.")