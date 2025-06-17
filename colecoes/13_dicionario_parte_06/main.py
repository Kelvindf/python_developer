# tupla
chaves = ('nome','Idade','E-mail','Profissão')
pessoas = [
    {
        chaves[0]:"kelvin",
        chaves[1]: 21,
        chaves[2]: "kelvin@gmail.com",
        chaves[3]: "CEO"
    },
    {
         chaves[0]:"Maria da Silva",
        chaves[1]: 28,
        chaves[2]: "maria@gmail.com",
        chaves[3]: "Assistente Administrativo"
    }
]
# inserindo novo dicionário
pessoa = {}

# inserindo dados no novo dicionário
try:
    for chave in chaves:
        if chave == "Idade":
            pessoa[chave] = int(input("Informe a Idade: "))
        else:
            pessoa[chave] = input(f"Informe{chave}: ")
    pessoas.append(pessoa) #type: ignore
    print(f"{pessoa.get(chaves[0])} inserida com sucesso.") #type:ignore        
except Exception as e:
    print(f"Não foi possivel cadastrar nova pessoa. {e}.")
finally:
    for pessoa in pessoas: # type: ignore
        for chave in pessoa:
            print(f"{chave}: {pessoa.get(chave)}.") #type: ignore
        print(f"\n{'-'*40}\n")

