"""
Crie um programa que receba o nome do usuário e a idade, e informe o menu abaixo:
Sala 1 - A Roda Quadrada - Livre
Sala 2 - A Volta dos Que Não Foram - 12 anos
Sala 3 - Poeira em Alto Mar - 14 anos
Sala 4 - As Tranças do Rei Careca - 16 anos
Sala 5 - A Vingança do Farngo Assado - 18 anos
O usuário deverá escolher a sala do filme que deseja assistir, e o programa deverá:
- Liberar a entrada do usuário e encerrar, caso o usuário tenha a idade mínima, ou maior.
- Bloquear a entrada do usuário e pedir para o mesmo escolher outro filme, caso não tenha a idade mínima.
"""
# TODO

#receba os dados
nome = input("Informe seu nome:")
idade= int(input("Informe sua idade:"))


#lista de filmes com idade mínima
print("Filmes disponíveis")
print("Sala 1 - A Roda Quadrada - Livre")
print("Sala 2 - A Volta dos Que Não Foram - 12 anos")
print("Sala 3 - Poeira em Alto Mar - 14 anos")
print("Sala 4 - As Tranças do Rei Careca - 16 anos")
print("Sala 5 - A Vingança do Farngo Assado - 18 anos")

while True:
    escolha = int(input("Informe número da sala desejada:"))

    if escolha == 1:
        print(f"Entrada permitida! Bom filme, {nome}")
        break
    elif escolha == 2:
        if idade >= 12:
            print(f"Entrada permitida! Bom filme, {nome}") 
            break
        else:
            print(f"Você não tem idade permitida para esse filme,escolha outro")


    elif escolha == 3:
        if idade >=14:
            print(f"Entrada permitida! Bom filme, {nome}")
            break
        else:
            print(f"Você não tem idade permitida para esse filme,escolha outro")    

    elif escolha == 4:
        if idade >=16:
            print(f"Entrada permitida! Bom filme, {nome}")
            break
        else:
            print(f"Você não tem idade permitida para esse filme,escolha outro")

    elif escolha == 5:
        if idade >=18:
            print(f"Entrada permitida! Bom filme, {nome}")
            break
        else:
             print(f"Você não tem idade permitida para esse filme,escolha outro")
    else:
        print(f"Opção inválida, tente novamente")
            



    
    
        


