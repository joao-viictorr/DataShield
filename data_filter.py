import pandas as pd

database = pd.read_csv("cota-parlamentar.csv")

database['datemissao'] = pd.to_datetime(database['datemissao'], errors='coerce')

filter_database = database[database['datemissao'].dt.year == 2020]

filter_database.to_csv("dados_2020.csv", index=False)
