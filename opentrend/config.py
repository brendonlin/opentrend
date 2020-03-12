import configparser


parser = configparser.ConfigParser()
parser.read("config.ini")
DB = parser["DATABASE"]

DB_HOST = DB.get("host")
DB_PORT = DB.get("port")
DB_USER = DB.get("user")
DB_PWD = DB.get("pwd")
