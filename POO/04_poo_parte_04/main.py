# biblioteca
import random


# classe 
class Pessoa:
    # contrutor
    def __init__(self, nome, email, profissao, humor): #type: ignore
        # atributos
        self.nome = nome
        self.email = email
        self.profissao = profissao
        self.humor = humor    
    # métodos
    def dar_boas_vindas(self):
        return "Boa tarde!"
    
    def cumprimentar(self):
        return f"Olá, eu me chamo {self.nome}. É um prazer!"
    
    def perguntar(self):
        return f"Qual o seu nome?"
    
    def cartao_de_visitas(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Profissão: {self.profissao}")

    def ofender(self): # type: ignore
        return f"Quem liga? Me erra! Vai ver se eu tô na esquina!"
    
# algoritmo principal
if __name__ == "__main__":
    # instancia de dois objetos
    usuario_masculino = Pessoa("", "", "", bool(random.getrandbits(1)))
    usuaria_feminino = Pessoa("", "", "", bool(random.getrandbits(1)))


    # seta os valores dos atributos do objeto masculino
    usuario_masculino.nome = input("Informe seu nome: ").title().strip()
    usuario_masculino.email = input("Informe seu e-mail: ").lower().strip()
    usuario_masculino.profissao = input("Informe sua profissão: ").strip()


      # seta os valores dos atributos do objeto feminino
    usuaria_feminino.nome = input("Informe seu nome: ").title().strip()
    usuaria_feminino.email = input("Informe seu e-mail: ").lower().strip()
    usuaria_feminino.profissao = input("Informe sua profissão: ").strip()

    # conversa
    print(f"Homem: -{usuario_masculino.dar_boas_vindas()}")
    print(f"Mulher: -{usuaria_feminino.dar_boas_vindas()}")
    print(f"Homem: -{usuario_masculino.perguntar()}")
    if usuaria_feminino.humor is True:
        print(f"Mulher: -{usuaria_feminino.cumprimentar()}")
        print(f"Mulher: -{usuaria_feminino.perguntar()}")
        usuario_masculino.humor = usuaria_feminino.humor
        print(f"Homem: -{usuario_masculino.cumprimentar()}")
        print(f"Homem: Bom humor = {usuario_masculino.cumprimentar()}")
        print("segue meu cartão de visitas: ")
        print(usuario_masculino.cartao_de_visitas())
    else:
        print(f"Mulher: -{usuaria_feminino.ofender()}")
        usuario_masculino.humor = usuaria_feminino.humor
        print(f"Homem: Bom humor = {usuario_masculino}")