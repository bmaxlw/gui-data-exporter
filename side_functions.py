import pyodbc as db


# [30.03.22]: MS SQL Connection
def sql_server_connect(database, server='5CD116MK2D',
                       driver='{ODBC Driver 17 for SQL Server}',
                       trusted='yes'):
    cursor = db.connect(f'DRIVER={driver};'
                        f'SERVER={server};'
                        f'DATABASE={database};'
                        f'Trusted_Connection={trusted};').cursor()
    return cursor