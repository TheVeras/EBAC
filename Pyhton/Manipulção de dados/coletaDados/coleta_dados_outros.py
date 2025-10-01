
import pymysql
import pandas as pd
from sqlalchemy import create_engine

def conexao_mysql(host, user, password, db, table):
    # criando a conexão
    conn = pymysql.connect(host=host, user=user, password=password, db=db)

    cursor = conn.cursor()

    # executar consulta
    query = f'SELECT * FROM {table} LIMIT 10'
    cursor.execute(query)

    # buscar resultados
    resultados = cursor.fetchall()

    # exibir os resultados
    print('Tabela MySQL: ')
    for linha in resultados:
        print(linha)

    # fechar conexão
    cursor.close()
    conn.close()

def df_conexao_mysql(host, user, password, db, table):
    # criando a conexão
    conn = create_engine('mysql+pymysql://' + user + ':' + password + '@' + host + '/' + db)
    #conn = pymysql.connect(host=host, user=user, password=password, db=db)

    # executar consulta
    query = f'SELECT * FROM {table}'
    df = pd.read_sql(query, conn)

    # exibir os resultados
    print('Tabela MySQL com DataFrame:\n ', df.head())

    # fechar conexão
    conn.dispose()
    #conn.close()
    return df

def conexao_excel(path):
    #Ler arquivo Excel
    df = pd.read_excel(path)
    print('Dados Excel: \n', df.head())

    #Escrever arquivo csv
    df.to_csv('dados.csv', index=False)

def conexao_csv(path):
    #Ler arquivo csv
    df = pd.read_csv(path)
    print('Dados CSV: \n', df.head())

    #Escrever arquivo json
    df.to_json('dados.json',orient = 'records', index=False)


#conexao_mysql('localhost', 'root', 'root', 'loja_informatica', 'cliente')
df_cliente = df_conexao_mysql('localhost', 'root', 'root', 'loja_informatica', 'cliente')
df_cliente.to_excel('dados.xlsx', index=False)

conexao_excel('dados.xlsx')
conexao_csv('dados.csv')
