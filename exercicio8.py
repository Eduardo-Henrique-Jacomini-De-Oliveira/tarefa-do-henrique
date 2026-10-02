estoque = [
    {"nome": "Notebook", "preco": 3500.00},
    {"nome": "Mouse", "preco": 45.00},
    {"nome": "Monitor", "preco": 850.00}
]

print("Produtos que custam mais de R$ 50,00:")

for produto in estoque:
    if produto["preco"] > 50.00:
        print(f"- {produto['nome']}")
