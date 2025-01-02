import psycopg2
#Database Connectivity
DB_CONFIG={
    "dbname":"employe",
    "user":"postgres",
    "password":"Password",
    "host":"localhost",
    "port":5432
}
def connect_db():
    """Connect to the postgresSQL database"""
    try:
        conn=psycopg2.connect(**DB_CONFIG)
        print("Connection Successfull")
        return conn
    except Exception as e:
        print("Error connecting to database",e)
        return None
connect_db()