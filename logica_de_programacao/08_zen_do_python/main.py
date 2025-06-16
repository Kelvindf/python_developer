


# TODO 

# Declaração de variáveis
x = float(input("informe o valor de x:").replace(",", "."))
y = float(input("informe o valor de y:").replace(",", "."))

# menu
print(f"{'-'*20} CALCULADORA PYTHON {'-'}")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operador = input("Informe a opção desejada:")

match operador:
     
      
      case "1":
        print(f"O resultado da soma é: {x+y}.")
      case "2":
        print(f"O resultado da subtração é: {x-y}.")

      case "3":
        print(f"O resultado da multiplicação é: {x*y}.")

      case "4":
        print(f"O resultado da divisão é: {x/y}.")

      case _:
        print(f"Operador inválido.")
      
