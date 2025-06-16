while True:
    nome = input("Informe seu nome:")
    idade = int(input("Informe sua idade:"))
    result = "é maior de idade." if idade >= 18 else "é menor de idade."
    

    print(f" {nome} {result}")

    repetir = input("Deseja verificar de novo? (s/n)").lower().strip()
    match repetir: 
      case "s":
            continue
      case "n":
            break
      case _:
              print("opção inválida.")
              break    
