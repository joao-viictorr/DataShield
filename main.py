import csv
import os

from data_filter import data_filter

caminho_csv = "dados_2020.csv"
if not os.path.isfile(caminho_csv):
    data_filter()

map_parlamentar = {}
contador_parlamentar = 1

map_estado_regiao = {
    "Norte": ["AC", "AM", "AP", "PA", "RO", "RR", "TO"],
    "Nordeste": ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"],
    "Centro-oeste": ["DF", "GO", "MS", "MT"],
    "Sudeste": ["ES", "MG", "RJ", "SP"],
    "Sul": ["PR", "RS", "SC"],
}


def anonimizar_parlamentar(nome):
    global contador_parlamentar

    if nome in map_parlamentar:
        return map_parlamentar[nome]
    else:
        novo_id = f"P{str(contador_parlamentar).zfill(3)}"
        map_parlamentar[nome] = novo_id
        contador_parlamentar += 1
        return anonimizar_parlamentar(nome)


def anonimizar_estado(uf):
    for regiao, estados in map_estado_regiao.items():
        if uf in estados:
            return regiao


def salvar_csv_anonimizado(lista_dados, caminho_saida):
    if not lista_dados:
        return

    chaves = lista_dados[0].keys()

    with open(caminho_saida, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=chaves)
        writer.writeheader()
        writer.writerows(lista_dados)

    print(f"CSV anonimizado salvo em {caminho_saida}")


def processar_csv(caminho_csv):
    lista_dados = []

    with open(caminho_csv, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for linha in reader:
            registro = {}

            for chave, valor in linha.items():
                if chave.lower() == "datemissao":
                    registro["ano"] = valor[:4]
                elif chave.lower() == "nummes":
                    registro["mes"] = valor or ""
                elif chave.lower() == "sgpartido":
                    registro["partido"] = valor or ""
                elif chave.lower() == "sguf":
                    registro["regiao"] = anonimizar_estado(valor) or ""
                elif chave.lower() == "txnomeparlamentar":
                    registro["parlamentar"] = anonimizar_parlamentar(valor) or ""
                elif chave.lower() == "txtdescricao":
                    registro["descricao"] = valor or ""
                elif chave.lower() == "vlrdocumento":
                    registro["valor_documento"] = valor or ""
                elif chave.lower() == "vlrglosa":
                    registro["valor_glosa"] = valor or ""
                elif chave.lower() == "vlrliquido":
                    registro["valor_liquido"] = valor or ""

            lista_dados.append(registro)

    return lista_dados


if not os.path.isfile('dados_2020_anonimizado.csv'):
    lista_dados = processar_csv(caminho_csv)
    salvar_csv_anonimizado(lista_dados, 'dados_2020_anonimizado.csv')
