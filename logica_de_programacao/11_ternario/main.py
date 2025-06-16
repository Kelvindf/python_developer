nome = input("informe seu nome:")
idade = int(input("Informe sua idade:"))

result = "é maior de idade." if idade >= 18 else "é menor de idade"

print(f"{nome} {result}")
