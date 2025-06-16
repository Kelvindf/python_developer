'''
programa que receba o nome e a média final de um
aluno foi aprovado, se ficou
de recuperação, ou se foi reprovado, com base em sua média final.

'''
# NOTE - a média deverá ser entre 0 e 10.
# NOTE - média de aprovação = 7. Recuperação = 5.
# TODO

# Declaração de variáveis

nome = input("informe o nome do aluno")
media = float(input("informe a média do aluno:").replace(",", "."))

# verifica se a média está dentro do intervalo
if media >= 0 and media <= 10:
    if media >= 7:
       print(f"{nome} está aprovado.")
    elif media >= 5:
       print(f"{nome} está de recuperação.")
    else:
       print(f"{nome} está reprovado.")
else:
    print("valor da média inválida.")
