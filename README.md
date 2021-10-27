# pyodbc
Scripts em python para consultas em banco de dados.

## Instalação do pyodbc

É necessária a instalação dos pacotes **python3-pip gcc-c++ python3-devel unixODBC-devel**:
```
yum install python3-pip gcc-c++ python3-devel unixODBC-devel
```
E posteriormente o **pyodbc**
```
pip3 install --user pyodbc
```
## Instalação dos Drivers ODBC

Para cada database é necessário a instalação dos driver ODBC no SO. Abaixo você encontra mais sobre como instalá-los:

### MySQL

Você deve ter o repositório MySQL Yum (Exemplo utilizando CentOS/RHEL 7. Para outras distros [clique aqui](https://dev.mysql.com/doc/connector-odbc/en/connector-odbc-installation-binary-unix.html)):
```
su root
yum update mysql-community-release
```
Instalando conector MySQL:
```
yum install mysql-connector-odbc
```
Configurando conector e arquivo *.ini*:
- Verifique se você já possui os pacotes *unixODBC* e *unixODBC-devel*, se não tiver os instale:
```
yum install -y unixODBC unixODBC-devel
```
- Após a instalação dos pacotes verifique as informações do unixODBC com:
```
odbcinst -j
```
- A saida será algo assim:
```
unixODBC 2.3.1
DRIVERS............: /etc/odbcinst.ini
SYSTEM DATA SOURCES: /etc/odbc.ini
FILE DATA SOURCES..: /etc/ODBCDataSources
USER DATA SOURCES..: /home/user/.odbc.ini
SQLULEN Size.......: 8
SQLLEN Size........: 8
SQLSETPOSIROW Size.: 8
```
- Configure o arquivo */etc/odbc.ini* com os dados do seu servidor MySQL
```
[DSN Name]
Driver       = /usr/local/lib/libmyodbc8a.so
Description  = Connector/ODBC 8.0 UNICODE Driver DSN
SERVER       = localhost
PORT         =
USER         = root
Password     =
Database     = test
OPTION       = 3
SOCKET       =
```
No Campo drive pode usar um dos nomes abaixo encontrados no arquivo */etc/odbcinst.ini*:
```
[MySQL]
Description=MySQL for ODBC 8.0
Driver=/usr/local/lib/libmyodbc8w.so
UsageCount=1

[ODBC Driver 17 for SQL Server]
Description=Microsoft ODBC Driver 17 for SQL Server
Driver=/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.5.so.2.1
UsageCount=2
```
## Conectando no Banco

Apos todas as configurações realizadas você pode conectar no banco de varias maneiras dependendo da [connection string](https://www.connectionstrings.com/) que você utilizar:

- Através do DSN name: ```cnxn = pyodbc.connect('DSN=test;PWD=password')```
- Através da connection string inteira:
```
cnxn = pyodbc.connect('DRIVER={MySql ODBC Driver};SERVER=localhost;DATABASE=mysql;UID=user;PWD=pass;charset=utf8mb4;'
```
