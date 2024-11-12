import pandas as pd
from datetime import timedelta
import traceback

def criar_df(arquivo_csv_original):
    try:
        df = pd.read_csv(arquivo_csv_original, sep="\t", encoding='ISO-8859-1')
        print("DataFrame Criado:")
        print(df.head())
        return df
    except Exception as e:
        print("Erro ao criar DataFrame:")
        print(e)
        traceback.print_exc()

def formatar_data_para_excel(data):
    data_inicial_excel = '01/01/1900'
    data_inicial_excel = pd.to_datetime(data_inicial_excel, format="%d/%m/%Y")
    data = data - data_inicial_excel + timedelta(days=1)
    return data.days

def formatar_df(df):
    try:
        df['QTD'] = df['QTD'].astype(int)
        df['DATA'] = pd.to_datetime(df['DATA'], format="%d/%m/%Y")
        df['DATA'] = df['DATA'].apply(formatar_data_para_excel)
        print("DataFrame após formatação:")
        print(df.head())
        return df
    except Exception as e:
        print("Erro ao formatar DataFrame:")
        print(e)
        traceback.print_exc()

def exportar_resultado_csv(df, nome_tabela_resultado):
    try:
        df.to_csv(nome_tabela_resultado, sep="\t")
        print("Arquivo CSV exportado com sucesso")
    except Exception as e:
        print("Erro ao exportar o  o arquivo CSV:")
        print(e)
        traceback.print_exc()


if __name__ == '__main__':
    try:
        arquivo_csv_original = 'tabela_ex1_python.csv'
        nome_tabela_resultado = 'Tabela_resultado_ex1.csv'
        df = criar_df(arquivo_csv_original)
        df = formatar_df(df)

        exportar_resultado_csv(df, nome_tabela_resultado)

    except Exception as e:
        print("Erro:")
        traceback.print_exc()
