import psutil
import pysensors as ps
import ast



class Sne(object):
    _info = []



    @staticmethod
    def getProcI():   # get processor info
        proc = [] #storage list
        proc.append(psutil.cpu_times()._asdict()) #gets scputimes(user, nice, system, idle, iowait, irq, softirq, steal, guest, guest_nice)

        proc.append({psutil.cpu_percent()}) #shows cpu load

        proc.append(psutil.cpu_times_percent()._asdict()) #shows procentile cpu load

        # логические

        a = psutil.cpu_count(logical=True)
        proc.append(ast.literal_eval(str(a))) #shows quantity of cpu log cores


        # физические
        a = psutil.cpu_count(logical=False)
        proc.append(ast.literal_eval(str(a))) #shows quantity of cpu real cores


        proc.append(psutil.cpu_stats()._asdict()) #shows cpu stats: ctx_switches, interrupts, soft_interrupts, syscalls

        # частота цпу
        proc.append(psutil.cpu_freq()._asdict()) #cpu freq current, min, max

        # поядерная
        proc.append(dict.fromkeys(psutil.cpu_freq(percpu=True))) #cpu freq for each core


        dictionary = {} #cpu load (%)
        q = psutil.getloadavg(), dictionary
        proc.append(q)
        # в процентах
        q = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
        proc.append(dict.fromkeys(q))
        proc.append(q)
        return proc

    @staticmethod
    def getMemI(): #get memory info
        mem = []
        mem.append(psutil.virtual_memory()._asdict())
        mem.append(psutil.swap_memory()._asdict())
        mem.append(psutil.Process().memory_full_info()._asdict())

        return mem

    @staticmethod
    def getDiscI(): #get disc info
        disc = []

        disc.append(dict.fromkeys(psutil.disk_partitions()))
        disc.append(psutil.disk_io_counters()._asdict())
        disc.append(psutil.disk_io_counters(perdisk=True))

        return disc

    @staticmethod
    def getNetI():#get net info
        net = []
        net.append(psutil.net_io_counters()._asdict())
        net.append(psutil.net_io_counters(pernic=True))

        net.append(dict.fromkeys(psutil.net_connections()))


        net.append(psutil.net_if_addrs())
        net.append(psutil.net_if_stats())
        return net

    @staticmethod
    def getSensI():#get temperature and fans info
        sen = []
        sen.append(psutil.sensors_temperatures(fahrenheit=False))
        sen.append(psutil.sensors_fans())
        sen.append(psutil.sensors_battery())
        return sen

    @classmethod
    def _getInfo(self): #get all info
        self._info.append(self.getProcI())
        self._info.append(self.getMemI())
        self._info.append(self.getDiscI())
        self._info.append(self.getNetI())
        self._info.append(self.getSensI())


    @classmethod
    def _toPrint(self): #prints info
        print(self._info)


class SneToString(Sne): #prints info as string
    @classmethod
    def _PrintToString(self):
        print(str(self._info))
