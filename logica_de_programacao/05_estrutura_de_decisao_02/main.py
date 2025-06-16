  # TODO 
"""
Crie um programa que recebe o nome, a idade e a altura do usuário,
e verifica se o usuário tem a idade e a altura
mìima para entrar no brinquedo. Caso não tenha, o programa
deverá barra a entrada do usuário
"""
# Declaração de viráreis
nome = input("Informe o nome do usuário")
idade = int(input("Informe a idade do usupário"))
altura = float(input("informe a altura do usuário").replace(",", "."))

# verifica a idade e a altura do usuário
if idade >= 12 and altura >= 1.10:
    print(f"A entrada de {nome} foi autorizada.")
else:
    print(f"A entrada de {nome} foi negada")