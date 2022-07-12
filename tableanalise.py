import pandas as pd


df = pd.read_csv('tabela_cadeiras_kabum.csv', sep=';')


pd.DataFrame(df)
print(df)