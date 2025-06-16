# Dicionário

usuario = {
    'nome': "Matheus",
    'idade': 24,
    'email': "matheus@gmail.com",
    'telefone': "11999999999",
    'profissao': "Programador"

}

# Usuário escolhe a chave que deseja alterar.

chave = input("Informe a chave que deseja alterar: ").strip().lower()

# Tratamento de exceção
try:
    if chave in usuario:
        usuario[chave] = input("Informe o novo valor: ").strip()
        print(f"Chave '{chave}' Encontrada com sucesso!")
    else:
        print("Não foi possível encontrar a chave informada.")

except Exception as e:
    print(f"Erro ao alterar o valor: {e}")

finally:

    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario.get(chave)}")    