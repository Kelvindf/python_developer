
while True: 
   
    #Declaração de variáveis
    x = float(input("Informe um número real"))
    y = float(input("Outro número real"))


    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")

    operador = input("Informe a opção desejada:")

    match operador:
        case "1":print(f"O RESULTADO DA SOMA É {x+y}")
        case "2":print(f"O RESULTADO DA SUBTRAÇÃO É {x-y}")
        case "3":print(f"O RESULTADO DA DIVISÃO É {x/y}")
        case "4":print(f"O RESULTADO DA MULTIPLICAÇÃO É {x*y}")
        case _:
          print("Opção inválida")



    repetir = input("Deseja verificar de novo? (s/n) ").lower().strip()
    match repetir:
      case "s": 
        continue  
      case "n":
        break      

    
      




   

       

