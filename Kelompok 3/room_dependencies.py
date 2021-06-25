from nameko.extensions import DependencyProvider
import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
class DatabaseWrapper:

    def __init__(self, connection):
        self.connection = connection


    def get_room(self, id_room_type):
        cursor = self.connection.cursor(dictionary=True)
        sql = "SELECT * FROM `room` WHERE id_room_type = {}".format((id_room_type))
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

     
class Database(DependencyProvider):
    connection_pool = None
    def __init__(self):
        try:
            self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="database_pool",
            pool_size=5,
            pool_reset_session=True,
            host='localhost',
            database='proyek soa 2',
            user='root',
            password=''
            )
        except Error as e :
            print ("Error while connecting to MySQL using Connection pool ", e)
    def get_dependency(self, worker_ctx):
        return DatabaseWrapper(self.connection_pool.get_connection())
