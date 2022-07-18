import mysql.connector

def mysqlauth():
    return mysql.connector.connect(host="database-1.csao36671tpd.us-east-1.rds.amazonaws.com", user="groot",
                                   password="JbEPGE73ECAp5FG6SbELnNaPUGbuDj0AxcGQ", database="tnstorage")


def jwtauth():
    return 'secrete'
