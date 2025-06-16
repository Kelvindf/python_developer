# Dicionário

pessoa = {
    'nome': 'Matheus',
    'idade': 24,
    'email': 'matheus@gmail.com'
    
    }

# Exibir os dados do dicionário
for dado in pessoa:
    print(f"{dado.capitalize()}: {pessoa.get(dado)}")