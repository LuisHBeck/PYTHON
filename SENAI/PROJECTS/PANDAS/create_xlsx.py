import pandas as pd

cars = {
    'brand': ['Fiat', 'Chevrolet', 'Ford'],
    'model': ['Marea', 'Chevette', 'Escort'],
    'year': [1999, 1978, 1997]
}

dataframe = pd.DataFrame(cars)

dataframe.to_excel('./xlsx_archives/Cars.xlsx', index=False)
dataframe.to_csv('./xlsx_archives/Cars.csv', index=False)
