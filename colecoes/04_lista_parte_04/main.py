# Declaração de variáveis
cidades= [
    "brasília",
    "rio de janeiro",
    "belo horizonte",
    "curitiba", 
    "porto alegre",
    "são paulo",
    "salvador",
    "fortaleza",
    "recife",
    "manaus",
    "goiania",
    "campinas"
    ]
# Usuário faz a pesquisa
pesquisa = input("Informe a cidade que deseja pesquisar: ").strip()

quantidade = cidades.count(pesquisa)

print(f"A cidade {pesquisa} foi encontrada {quantidade} vezes na lista.")