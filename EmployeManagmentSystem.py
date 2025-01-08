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
#add_employee('Aarti','Accountant',4000000)

def view_employees():
    query="SELECT * FROM emp"
    conn=connect_db()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query)
                emp=cursor.fetchall()
                print("\n Employee List")
                for eone in emp:
                    print(f"Id:{eone[0]},name:{eone[1]},position:{eone[2]},salary:{eone[3]}")
        except Exception as e:
            print("Error adding emp",e)
        finally:
            conn.close()
view_employees()

def update_employee(empid,name=None,position=None,salary=None):
    query="UPDATE emp SET name=COALESCE(%s,name),position=COALESCE(%s,position),salary=COALESCE(%s,salary) WHERE id=%s"
    conn=connect_db()
    if conn:
        try:
            with conn.cursor()as cursor:
                cursor.execute(query,(name,position,salary,empid))
                conn.commit()
                print("Employee added succesfully")
        except Exception as e:
            print("Error Updating",e)
        finally:
            conn.close()
#update_employee(1,"Akki","Manager",300)
            
                
                
    