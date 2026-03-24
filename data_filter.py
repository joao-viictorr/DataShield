import pandas as pd

def data_filter():
    database = pd.read_csv("cota-parlamentar.csv")
    database['datemissao'] = pd.to_datetime(database['datemissao'], errors='coerce')

    filter_database = database[
        (database['datemissao'].dt.year == 2020) &
        (database['idecadastro'].notna()) &
        (database['idecadastro'] != '')
    ]
    filter_database.to_csv("dados_2020.csv", index=False)
