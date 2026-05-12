import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - Line:%(lineno)d - %(message)s"
)
import mysql.connector

connetion =mysql.connector.connect(host="localhost",user="root",password="")
logging.info(f"{connetion}")