from pymongo import MongoClient
conn = MongoClient(host="34.199.33.217",port=27017)
db = conn['db_Nition']
try:
    server_info= conn.server_info();
    print("conexion exitosa ")
except Exception as e:
    print("Error al conectar ",str(e))