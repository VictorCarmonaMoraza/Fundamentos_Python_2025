import pandas as pd

datafarme1 = pd.read_csv(r'C:\Users\Victo\Desktop\IPA Automatizacion de Procesos Inteligentes con Python\iris_dataset.csv',
                           delimiter=',', encoding='iso-8859-1')

print(datafarme1.head())


dataframe2=pd.read_excel(r'C:\\Users\\Victo\\Desktop\\IPA Automatizacion de Procesos Inteligentes con Python\\Distrito_poblacion.xlsx', sheet_name='Distrito_poblacion')
print(dataframe2.head())