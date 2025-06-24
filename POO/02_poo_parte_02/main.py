# classe
class Pessoa:
    nome = "Alex machado"
    idade = 40
    email = "alex@gmail.com"
    profissao = "programador"

    # métodos
    def apresentar(self):
        print(f"Olá,meu nome é {self.nome}, tenho {self.idade} anos,trabalho com {self.profissao} e meu e-mail é {self.email}.")
    
# algoritmo principal
if __name__ == "__main__":
    # instancia a classe
    usuario = Pessoa()

    # executar o método
    usuario.apresentar()