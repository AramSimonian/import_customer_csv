import dbsettings as dbs
import mysql.connector
from mysql.connector import Error

def connect_db():
    cur = None
    try:
        conn = mysql.connector.connect(user=dbs.connection_properties['user'],
                                        password = dbs.connection_properties['password'],
                                        host=dbs.connection_properties['host'],
                                        database=dbs.connection_properties['db_name'],
                                        port=dbs.connection_properties['port'])

        cur = conn.cursor()

    except Exception as e:
        print(e)

    finally:
        return cur