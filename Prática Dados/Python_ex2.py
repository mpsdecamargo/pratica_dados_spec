import pandas as pd
import os
import traceback

def criar_df(arquivo_csv_original):
    try:
        df = pd.read_csv(arquivo_csv_original, sep=";", header=None, encoding='ISO-8859-1')
        print("DataFrame Criado:")
        print(df.head())
        return df
    except Exception as e:
        print("Erro ao criar DataFrame:")
        print(e)
        traceback.print_exc()

def renomear_colunas_df(df):
    try:
        df.columns = ["Cliente", "Acao", "QTD", "Preco"]
        print("DataFrame após renomear colunas:")
        print(df.head())
        return df
    except Exception as e:
        print("Erro ao renomear colunas:")
        print(e)
        traceback.print_exc()

def formatar_df(df):
    try:
        df.drop(0, inplace=True)
        df["Cliente"] = df["Cliente"].astype(int)
        df["QTD"] = df["QTD"].astype(int)
        df["Preco"] = df["Preco"].astype(float)
        print("DataFrame após formatação:")
        print(df.head())
        return df
    except Exception as e:
        print("Erro ao formatar DataFrame:")
        print(e)
        traceback.print_exc()

def criar_df_resultado(df):
    try:
        df2 = df.copy()
        df2["Total"] = df2["QTD"] * df2["Preco"]
        resultado = df2.groupby("Cliente").agg({
            "Total": 'sum'
        })
        resultado.rename(columns={'Total': 'Financeiro em ações'}, inplace=True)
        resultado.reset_index()
        print("Resultado do agrupamento por Cliente:")
        print(resultado.head())
        return resultado
    except Exception as e:
        print("Erro ao criar resultado do DataFrame:")
        print(e)
        traceback.print_exc()

def exportar_resultado_csv(resultado, nome_tabela_resultado):
    try:
        resultado.to_csv(nome_tabela_resultado, index=True, sep=";")
        print("Arquivo CSV exportado com sucesso")
    except Exception as e:
        print("Erro ao exportar o  o arquivo CSV:")
        print(e)
        traceback.print_exc()


if __name__ == '__main__':
    try:
        arquivo_csv_original = 'Teste_Specialisterne_Oct2024.csv'
        nome_tabela_resultado = 'Tabela_resultado_cliente_financero_em_acoes.csv'
        df = criar_df(arquivo_csv_original)
        df = renomear_colunas_df(df)
        df = formatar_df(df)
        resultado = criar_df_resultado(df)
        exportar_resultado_csv(resultado, nome_tabela_resultado)

    except Exception as e:
        print("Erro:")
        traceback.print_exc()