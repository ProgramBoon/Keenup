import psycopg2
import cre2

class Database:
    def __init__(self):

        p = cre2.XML('ui')
        dbn =  p.parsingFile("database",True)
        us = p.parsingFile("user",True)
        pas = p.parsingFile("password",True)
        hos = p.parsingFile("host",True)

        try:
            conn = psycopg2.connect(dbname = dbn,user = us,password= pas,host = hos)
        except:
            print ("I am unable to connect to the database.")


