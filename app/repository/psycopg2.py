from psycopg2 import pool
import logging
import logger_config

logger = logging.getLogger(__name__)
class repository:
    def __init__(self):
        logger.info("Initializing psycopg2 pool")
        self.pool = pool.SimpleConnectionPool(3, 3,host= "db", 
                            database="postgres", user="admin",
                            password="password")
    def create_item(self, name:str, price:int) -> None:
        logger.info("Creating item")
        conn = self.pool.getconn() 
        cur = conn.cursor()
        cur.execute("insert into items(name,price) values (%s,%s);", (name,price))
        conn.commit()
        cur.close()
        self.pool.putconn(conn)
        logger.info("Item created")
    def __del__(self):
        self.pool.closeall()
def initialize_repository():
    return repository()
