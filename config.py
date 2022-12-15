from dotenv import load_dotenv

import os
load_dotenv()
user = os.environ["MYSQL_USER"]
password = os.environ["MYSQL_PASSWORD"]
secretKey = os.environ["APP.SECRET_KEY"] 
database = os.environ["MYSQL_DATABASE"]

SQL_DATABASE_URI = f'mysql://{user}:{password}@localhost/{database}'