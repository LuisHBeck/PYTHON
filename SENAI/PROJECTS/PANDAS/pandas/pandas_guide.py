import pandas as pd

vendas = {'data': ['15/02/2023', '16/05/2023'],
          'valor': [500, 300],
          'produto': ['feijão', 'arroz'],
          'qnt': [50, 70]}

# vendas_df = pd.DataFrame(vendas)
# print(vendas_df)

vendas_df = pd.read_excel("Vendas.xlsx")
print(vendas_df.head()) #firts five lines
print(vendas_df.shape) #quantity of lines and columns
print(vendas_df.describe()) # resum of numerics columns 
