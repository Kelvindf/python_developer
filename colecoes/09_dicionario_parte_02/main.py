# Dicionário

pessoa = {
    'nome': "",
    'idade':"",
    'email':"",
    }

# Exibi dados
print(f"Nome: {pessoa['nome']}")
print(f"E_mail: {pessoa.get('email')}")

# Exibe os dados inexistente
print(f"Idade: {pessoa.get('idade')}")


# Inserindo a idade da pessoa
try:
    pessoa['email'] = int(input("Informe o e-email: "))
except Exception as e:
    print(f"Não foi possível inserir um novo valor. {e}.")
finally:
    print(f"Nome: {pessoa.get('nome')}")
    print(f"E-mail: {pessoa.get('email')}")
    print(f"Idade: {pessoa.get('idade')}")        