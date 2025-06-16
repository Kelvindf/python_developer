try:
    # TODO
    n = int(input("Informe um número inteiro positivo:"))

    while n > 0:
        print(n)
        n -= 1
except Exception as e:
    print(f"Não foi possível fazer a contagem.")
finally:
    print("Programa encerrado")      