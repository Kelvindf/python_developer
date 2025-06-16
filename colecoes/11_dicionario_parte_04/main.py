usuario = {
    'nome': "Matheus",
    'idade': 24,        
    'email': "matheus@gmail.com",
    'profissao': "Programador",

}

# Usuário escolhe a chave que deseja deletar.
chave = input("Informe a chave que deseja deletar: ").strip().lower()


# Tratamento de exceção
try: 
    if chave in usuario:
        del usuario[chave]
        print(f"Chave deletada com sucesso!")
    else:
        print("Não foi possível encontrar a chave informada.")

except Exception as e:

    print(f"Erro ao deletar a chave: {e}")

finally:
# Exibe os valores do dicionario

    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario.get(chave)}")
