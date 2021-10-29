import pyodbc
from pssw import *
import argparse

parser = argparse.ArgumentParser(
                description="SQL Query Script")

parser.add_argument("--server", dest="server",
                        help="Instancia para realizar a query",
                        required=True, type=str)

args = parser.parse_args()

ConnectionString = "DRIVER=MySQL ODBC 8.0 ANSI Driver;SERVER={1};DATABASE=db;UID=user;PWD={0};OPTION=3;CHARSET=utf8mb4;".format(pwdins1, args.server)

"""Informações da conexão com o servidor MySQL"""
cnxn = pyodbc.connect(ConnectionString)

"""Define a codificação de caracteres"""
cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
cnxn.setencoding(encoding='utf-8')
cursor = cnxn.cursor()

"""Definindo a query dentro da função execute()"""
cursor.execute("SELECT eventid FROM zabbix.alerts order by eventid limit 1;")
"""Utilizando o método fetchval() para obter o primeiro valor da primeira linha"""
row = cursor.fetchval()
"""Mostra o valor que vou coletado"""
if row:
    print(row)
    
"""Observação: esse script foi feito para coletar o último valor de uma query
com o objetivo de armazená-lo em outra base para monitoração"""
