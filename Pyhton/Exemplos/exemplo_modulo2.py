# Exemplo de uso de listas e dicionários em Python

# Lista de registros de vendas
vendas = [
    {"produto": "A", "quantidade": 10, "preco": 5.0},
    {"produto": "B", "quantidade": 5, "preco": 7.5},
    {"produto": "C", "quantidade": 8, "preco": 3.0}
]

# Dicionário para mapear IDs de produtos para detalhes
produtos = {
    "A": {"nome": "Produto A", "categoria": "Categoria 1"},
    "B": {"nome": "Produto B", "categoria": "Categoria 2"},
    "C": {"nome": "Produto C", "categoria": "Categoria 1"}
}

# Calcular receita total
receita_total = 0
for venda in vendas:
    receita_total += venda["quantidade"] * venda["preco"]

print(f"Receita Total: {receita_total}")

# Exibir detalhes dos produtos vendidos
for venda in vendas:
    produto_id = venda["produto"]
    detalhes = produtos[produto_id]
    print(f"Produto: {detalhes['nome']}, Categoria: {detalhes['categoria']}, Quantidade Vendida: {venda['quantidade']}")
    