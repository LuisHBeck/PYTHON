import pandas as pd


tabela = pd.read_excel("./xlsx_archives/Produtos.xlsx")
print(tabela)
print()

tabela.loc[tabela['Tipo']=='Serviço', 'Multiplicador Imposto'] = 1.5
tabela['Preço Base Reais'] = tabela['Preço Base Original'] * tabela['Multiplicador Imposto']
print(tabela)

tabela.to_excel('./xlsx_archives/New_Produtos.xlsx', index=False, sheet_name='NewProdutos')