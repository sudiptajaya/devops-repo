from loguru import logger
import mysql.connector

from src.main.encrypt_decrypt12.encrypt_decrypt import decrypt

class MySqlConnector:
   def __init__(self,config):
      self.config = config
      self.connection = None
      
   def connect (self): 
        try:     
            self.connection = mysql.connector.connect(host = self.config["mysql_database"]["host"],
                                     user = self.config["mysql_database"]["user"],
                                     password = decrypt(self.config["mysql_database"]["password"]),
                                     database = self.config["mysql_database"]["database"])
            logger.info("connection sucessfull")
        except Exception as e:
            logger.error(f"error occure: {e}")    
            raise e
   def closer(self):
       if self.connection.is_connected():
           self.connection.close()
           logger.info("connectiom is closed")
           
  

class MySqlCRUDoperation:
    def __init__(self,mysql_connection):
        self.connection = mysql_connection
    def read_from_mysql(self,query):
           try:

    #    logger.info(f"{connection}")

            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            logger.info(f"{result}")
            return result
    #    logger.info("query is done in the database")
           except Exception as e:
            logger.info(f"error occure in mysql_db{e}")
            raise e   
           

    def insert_from_mysql(self,query):
           try:

    #    logger.info(f"{connection}")

            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            logger.info(f"{result}")
            return result
    #    logger.info("query is done in the database")
           except Exception as e:
            logger.info(f"error occure in mysql_db{e}")
            raise e         
        



# def read_from_mysql(config, query):
#    try:

#     #    logger.info(f"{connection}")

#        cursor = connection.cursor()
#        cursor.execute(query)
#        result = cursor.fetchall()
#        logger.info(f"{result}")
#        return result
#     #    logger.info("query is done in the database")
     
#    finally:
   
#     #  connection.commit()
#      connection.close()
#      cursor.close()
# insert_query= 