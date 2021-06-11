import sys
import os
sys.path.append(os.getcwd()+'/Keenup.lib')
import sne
import database
import cre2
import cron
import getpass
from tmpw import app


# делаем хмл
p = cre2.XML('ui')
p.createFile()
# period in cre2
getinf = cron.ScheduleManager()
getinf.run()




# проверяем подключение - ничего, значит ок, ошибка - не подключились
# p = database.Database()
# # p.insert_data(sne.Sne._ret())
# p.alarm()
app.run()
# sne.SneToString._PrintToString()



