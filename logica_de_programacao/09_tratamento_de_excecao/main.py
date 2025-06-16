# tratanento de exceção
try: 

    numero = int(input("Informe um número inteiro"))
    
    print(f"O número informado é {numero}.")
except Exception as e:
    print(f"Não foi possível imprimir o número.{e}")
finally:
    print("Programa encerrado.")