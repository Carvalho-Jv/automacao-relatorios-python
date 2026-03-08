import pandas as pd

# Carregar dados
dados = pd.read_csv("vendas.csv")

# Calcular indicadores
faturamento_total = dados["valor"].sum()
vendas_por_produto = dados.groupby("produto")["valor"].sum()

print("Faturamento total:", faturamento_total)
print("\nVendas por produto:")
print(vendas_por_produto)

# Salvar relatório
vendas_por_produto.to_csv("relatorio_produtos.csv")
