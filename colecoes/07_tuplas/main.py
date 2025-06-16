estados = (
    "distrito federal",
    "são paulo",
    "rio de janeiro",
    "minas gerais",
    "paraná",
    "rio grande do sul"
)

for estado in estados:
    print(estado)

estado_pesquisa = input("Informe um estado que deseja pesquisar:").title().strip()
qtde_estados = estados.count(estado_pesquisa)

print(f"{estado_pesquisa} foi encontrado {qtde_estados} vez(es) na tupla.")


try:
    estados.sort()
    for estado in estados:
        print(estado)
except Exception as e:
    print(f"Erro ao tentar ordenar a tupla: {e}")
