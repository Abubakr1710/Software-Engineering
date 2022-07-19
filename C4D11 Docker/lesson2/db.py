from sqlalchemy import create_engine
import pandas as pd

def create_db():
    try:
        engine = create_engine("sqlite:///C4D11 Docker/lesson2/student.db")
        conn = engine.connect()

        df = pd.read_csv("C4D11 Docker/lesson2/students.csv")
        df.to_sql('C4D11 Docker/lesson2/students', conn, if_exists='replace')
        conn.close()
        return 0
    except:
        return 1

def get_students():
    try:
        engine = create_engine("sqlite:///C4D11 Docker/lesson2/student.db")
        conn = engine.connect()

        df = pd.read_sql_query("SELECT * FROM students", conn)
        conn.close()
        return df.to_dict()
    except:
        return {'Error':'No table found'}

def get_name(email):
    try:
        engine = create_engine("sqlite:///C4D11 Docker/lesson2/student.db")
        conn = engine.connect()

        df = pd.read_sql_query("SELECT name FROM students WHERE email = '{}'".format(email), conn)
        conn.close()
        return df.to_dict()
    except:
        return {'Error':'No email found'}

create_db()  