import psycopg2
import cre2

class Database:
    _conn = 0
    def __init__(self):

        p = cre2.XML('ui')
        dbn =  p.parsingFile("database",True)
        us = p.parsingFile("user",True)
        pas = p.parsingFile("password",True)
        hos = p.parsingFile("host",True)
        try:
            self.conn = psycopg2.connect(dbname = dbn,user = us,password= pas,host = hos)
        except:
            print ("I am unable to connect to the database.")

    def insert_data(self, data):
        """ insert multiple vendors into the vendors table  """
        sql = "INSERT INTO datacatch(pcid, keyname, value) VALUES(1, %s, %s)"

        self.conn = None
        try:

                # create a new cursor
                cur = self.conn.cursor()

                for i in data:
                    cur.execute(sql, (i, data[i]))

                # commit the changes to the database
                self.conn.commit()
                # close communication with the database
                cur.close()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
        finally:
            if self.conn is not None:
                self.conn.close()


