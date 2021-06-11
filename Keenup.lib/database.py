import psycopg2
import cre2
import datetime
import Keenbot

class Database:
    _conn = 0
    def __init__(self):

        p = cre2.XML('ui')
        dbn =p.parsingFile("database",True)
        us = p.parsingFile("user",True)
        pas = p.parsingFile("password",True)
        hos = p.parsingFile("host",True)
        try:
            self.conn = psycopg2.connect(dbname = dbn,user = us,password= pas,host = hos)
        except:
            print ("I am unable to connect to the database.")

    def insert_data(self, data):
        """ insert multiple vendors into the vendors table  """
        sql = "INSERT INTO datacatch(keyname , value) VALUES(%s, %s)"
        datesql = "INSERT INTO public.date(date) VALUES(%s);"
        self.conn = None
        try:
            p = cre2.XML('ui')
            dbn = p.parsingFile("database", True)
            us = p.parsingFile("user", True)
            pas = p.parsingFile("password", True)
            hos = p.parsingFile("host", True)

            date_object = "\'"+str(datetime.date.today())+"\'"
            print(date_object)

            try:
                self.conn = psycopg2.connect(dbname=dbn, user=us, password=pas, host=hos)

                # create a new cursor
                cur = self.conn.cursor()
                cur.execute(datesql, (date_object,))
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

    def alarm(self):
        sql = "SELECT * FROM public.log;"
        sqlupdate = "UPDATE public.log SET alarm = FALSE WHERE alarm = 'TRUE';"
        self.conn = None
        try:
            p = cre2.XML('ui')
            dbn = p.parsingFile("database", True)
            us = p.parsingFile("user", True)
            pas = p.parsingFile("password", True)
            hos = p.parsingFile("host", True)
            try:
                self.conn = psycopg2.connect(dbname=dbn, user=us, password=pas, host=hos)
                # create a new cursor
                cur = self.conn.cursor()
                cur.execute(sql)
                x = cur.fetchall()
                for i in x:
                    if i[3] is True:
                        tex = 'тревога в ' + str(i[4])+' сенсор '+str(i[0])+' время '+ str(i[1])+ ' id в datacatch: '+ str(i[2])
                        Keenbot.send_telegram(tex)
                        cur.execute(sqlupdate)
                self.conn.commit()

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def alarmlast(self):
        sql = "SELECT * FROM (SELECT * FROM log ORDER BY id DESC LIMIT 10) sub ORDER BY id ASC;"
        self.conn = None
        try:
            p = cre2.XML('ui')
            dbn = p.parsingFile("database", True)
            us = p.parsingFile("user", True)
            pas = p.parsingFile("password", True)
            hos = p.parsingFile("host", True)
            try:
                self.conn = psycopg2.connect(dbname=dbn, user=us, password=pas, host=hos)
                # create a new cursor
                cur = self.conn.cursor()
                cur.execute(sql)
                x = cur.fetchall()
                self.conn.commit()
                return(x)
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
