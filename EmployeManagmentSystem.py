import psycopg2
#Database Connectivity
DB_CONFIG={
    "dbname":"employeeone",
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
#connect_db()

def add_employee(name,position,salary):
    """AA employe data to database"""
    query="INSERT INTO emp(name,position,salary) VALUES(%s,%s,%s)"
    conn=connect_db()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query,(name,position,salary))
                conn.commit()
                print("successfull")
        except Exception as e:
            print("error adding employe",e)
        finally:
            conn.close()
add_employee('Asha','HR',30000000)
            
                
                
    