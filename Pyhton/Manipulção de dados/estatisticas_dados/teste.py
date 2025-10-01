import pandas as pd
import numpy as np

# parâmetros
teto = 2250
meses = 30
valor_construtora = 33000
parcelas_anuais = {12: 5000, 24: 5000, 30: 5000}

# % da obra de 2% a 100% linear
percentuais = np.linspace(0.02, 1.0, meses)

# parcela de obra
parcela_obra = percentuais * teto

# parcela construtora distribuída linearmente
parcela_construtora_base = valor_construtora / meses
parcela_construtora = np.full(meses, parcela_construtora_base)

# corrigir para respeitar teto
for i in range(meses):
    if parcela_obra[i] + parcela_construtora[i] > teto:
        parcela_construtora[i] = teto - parcela_obra[i]

# ajuste final para somar exatamente 33 mil
fator = valor_construtora / parcela_construtora.sum()
parcela_construtora *= fator

# calcular totais mensais
totais = []
for i in range(meses):
    anual = parcelas_anuais.get(i+1, 0)
    total = parcela_obra[i] + parcela_construtora[i] + anual
    totais.append(total)

# montar dataframe
df = pd.DataFrame({
    "Mês": np.arange(1, meses+1),
    "% Obra": (percentuais*100).round(2),
    "Parcela Obra (R$)": parcela_obra.round(2),
    "Parcela Construtora (R$)": parcela_construtora.round(2),
    "Parcela Anual (R$)": [parcelas_anuais.get(i+1, 0) for i in range(meses)],
    "Total (R$)": np.array(totais).round(2)
})

# adicionar resumo
resumo = pd.DataFrame({
    "Mês": ["Total Geral"],
    "% Obra": [""],
    "Parcela Obra (R$)": [df["Parcela Obra (R$)"].sum().round(2)],
    "Parcela Construtora (R$)": [df["Parcela Construtora (R$)"].sum().round(2)],
    "Parcela Anual (R$)": [df["Parcela Anual (R$)"].sum().round(2)],
    "Total (R$)": [df["Total (R$)"].sum().round(2)]
})

df_final = pd.concat([df, resumo], ignore_index=True)

# salvar em Excel
caminho_arquivo = "fluxo_caixa_30_meses.csv"
df_final.to_csv(caminho_arquivo, index=False)

print(f"Arquivo gerado com sucesso: {caminho_arquivo}")
