# classes 
class Pessoa:
    # atributos
    nome = "Alex Machado"
    idade = 40
    email = "alaex@gmail.com"
    profissao = "programador"

# algoritmo principal
if __name__ == "__main__":
    # instancia a classe Pessoa (cria objeto da classe)
    usuario = Pessoa()

    # exibe na tela os dados do usuário
    print(f"Nome: {usuario.nome}.")
    print(f"Idade: {usuario.idade}.")
    print(f"E-mail: {usuario.email}.")
    print(f"Profissão: {usuario.profissao}.")
    
