"""Faz o import do pacote pyodbc"""
"""https://github.com/mkleehammer/pyodbc"""
import pyodbc


"""Informações da conexão com o servidor MySQL"""
cnxn = pyodbc.connect('DRIVER={MySql ODBC Driver};'
                      'SERVER=localhost;'
                      'DATABASE=mysql;'
                      'UID=user;'
                      'PWD=pass'
                      'charset=utf8mb4;')

"""Define a codificação de caracteres"""
cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
cnxn.setencoding(encoding='utf-8')

cursor = cnxn.cursor()


"""Definindo a query dentro da função execute()"""
cursor.execute("select user_id, user_name from users")
"""Utilizando o método fetchval() para obter o primeiro valor da primeira linha"""
row = cursor.fetchone()
"""Mostra o valor que vou coletado"""
if row:
    print(row)
    
"""Observação: esse script foi feito para coletar o último valor de uma query
com o objetivo de armazená-lo em outra base para monitoração"""
