# função
def dar_boas_vindas(nome): #type:ignore
    return f"Seja bem vindo {nome}!!!"

# algoritmo principal
nome = input("Informe seu nome: ")
print(dar_boas_vindas(nome))