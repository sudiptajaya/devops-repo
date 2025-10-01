from src.main.database.mysql_connector import *

import configparser
config=configparser.ConfigParser()
config.read(r"D:\my_init\src\resources\config.ini")

def main():
   mysql_db_connection = MySqlConnector(config) 
   mysql_db_connection.connect()
   crud_operation_obj = MySqlCRUDoperation(mysql_db_connection.mysql_connection)
   query="select * from labours_table"
   final_result=read_from_mysql(config,query)
   logger.info(f"{final_result}")
   



if __name__== "__main__":
   main()