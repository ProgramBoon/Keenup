import sys
import os
sys.path.append(os.getcwd()+'/Keenup.lib')
import sne
import database
import cre2



sne.Sne._getInfo()

sne.Sne._toPrint()

# делаем хмл
p = cre2.XML('ui')
p.createFile()
# проверяем подключение - ничего, значит ок, ошибка - не подключились
p = database.Database()


# sne.SneToString._PrintToString()



