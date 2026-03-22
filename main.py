import csv

map_parlamentar = {}
contador_parlamentar = 1

map_estado_regiao = {
    "norte": ["AC", "AM", "AP", "PA", "RO", "RR", "TO"],
    "nordeste": ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"],
    "centro-oeste": ["DF", "GO", "MS", "MT"],
    "sudeste": ["ES", "MG", "RJ", "SP"],
    "sul": ["PR", "RS", "SC"],
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

caminho_csv = "dados_2020.csv"
lista_dados = processar_csv(caminho_csv)

i = 0
for dado in lista_dados:
    print(dado)

    i += 1

    if i == 100:
        break
