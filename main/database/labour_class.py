from loguru import logger
import configparser
from src.main.database.mysql_connector import MySqlConnector, MySqlCRUDoperation
class labour:
    
    def __init__(self,last_name, first_name, wages, role):

        self.first = first_name
        self._last = last_name
        self.__wages = wages
        self.role = role
    def save_to_database(self,crud):
        print(self.__wages)
        pass 
        query = "SELECT ID from labours WHERE lower(first_name) = %s AND lower(last_name) =%s"
        result = self.crud.read_from_mysql(query, (self.first_name, self.last_name))
        if result:
            logger.info(f"labour already exist :{result[0][0]}")
            return result[0][0]
        insert_query = """ INSER INTO labours(first_name, last_name, wages, role, email)
        VALUES (%s. %s, %s, %s, %s)
        """
        email = self.first_name + "." + self.last_name +"@gmail.com"
        crud.insert_into_mysql(insert_query,(self.first_name, self.last_name, self.wages, self.role, None))
        result = crud.read_from_mysql(query, (self.first_name, self.last_name))
        logger.info(f"new labour added with ID :{result[0][0]}")
        return result[0][0]
    def login(self):
        pass   

config=configparser.ConfigParser()
config.read(r"D:\my_init\src\resources\config.ini")
mysql_db_conn_obj = MySqlConnector(config)    
mysql_db_conn_obj.connect()
crud = MySqlCRUDoperation(mysql_db_conn_obj.connection)
sudipta_obj = labour("Sudipta", "Bhandari", 900)  
sudipta_obj.save_to_database(crud) 
print(sudipta_obj._labour__wages)     