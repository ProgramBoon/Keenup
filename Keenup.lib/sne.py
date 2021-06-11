import psutil
import pysensors as ps
import ast



class Sne(object):
    _info = {}


    def dict_add_keep_last(a, b):  # aka merged() or updated()
        merged = {a, b}
        return merged

    @classmethod
    def getProcI(self):   # get processor info
        proc = {} #storage list
        proc = (psutil.cpu_times()._asdict()) #gets scputimes(user, nice, system, idle, iowait, irq, softirq, steal, guest, guest_nice)

        # proc.append('cpu_percent:')
        x = {'cpu_percent': psutil.cpu_percent()} #shows cpu load
        proc = {**proc, **x}
        # x('cpu_times_percent')
        x = (psutil.cpu_times_percent()._asdict()) #shows procentile cpu load

        for key in list(x.keys()):
            x[key +'_percent'] = x.pop(key)

        proc = {**proc, **x}
         # логические
        x = {'cpu_count(logical)': psutil.cpu_count(logical=True)}
        proc = {**proc, **x}
        # # физические
        x = {'cpu_count(physical)': psutil.cpu_count(logical=False)}
        proc = {**proc, **x}

        proc = {**proc, **psutil.cpu_stats()._asdict()}#shows cpu stats: ctx_switches, interrupts, soft_interrupts, syscalls
        # # частота цпу

        proc = {**proc, **psutil.cpu_freq()._asdict()} #cpu freq current, min, max
        #
        # # поядерная
        proc = {**proc, **dict.fromkeys(psutil.cpu_freq(percpu=True))} #cpu freq for each core


        q = psutil.getloadavg()
        proc = {**proc, **{'loadavg1':q[0],'loadavg5':q[1],'loadavg15':q[2]}}

        # в процентах
        q = [x / psutil.cpu_count() * 100 for x in psutil.getloadavg()]
        proc = {**proc, **{'loadpercent1':q[0],'loadpercent5':q[1],'loadpercent15':q[2]}}
        return proc

    @staticmethod
    def getMemI(): #get memory info
        mem = {}
        mem = {**mem, **psutil.virtual_memory()._asdict()}
        mem = {**mem, **psutil.swap_memory()._asdict()}
        mem = {**mem, **psutil.Process().memory_full_info()._asdict()}
        return mem

    @staticmethod
    def getDiscI(): #get disc info
        disc = {}

        # disc.append(dict.fromkeys(psutil.disk_partitions()))
        disc = {**disc, **psutil.disk_io_counters()._asdict()}
        # disc.append(psutil.disk_io_counters(perdisk=True))

        return disc

    @staticmethod
    def getNetI():#get net info
        net = {}
        net = {**net, **psutil.net_io_counters()._asdict()}
        # net.append(psutil.net_io_counters(pernic=True))

        net = {**net, **dict.fromkeys(psutil.net_connections())}


        net = {**net, **psutil.net_if_addrs()}
        net = {**net, **psutil.net_if_stats()}
        return net

    # @staticmethod
    # def getSensI():#get temperature and fans info
    #     sen = {}
    #     x = (psutil.sensors_temperatures(fahrenheit=False))
    #     q = {}
    #     for val in list(x.values()):
    #         for item in len(val):
    #             q =
    #
    #
    #
    #     sen = {**sen, **psutil.sensors_temperatures(fahrenheit=False)}
    #     sen = {**sen, **psutil.sensors_fans()}
    #
    #     sen = {**sen, **{'battery': psutil.sensors_battery()}}
    #     return

    @classmethod
    def _getInfo(self): #get all info
        self._info = {**self._info, **self.getProcI()}
        self._info = {**self._info, **self.getMemI()}
        # self._info = {**self._info, **self.getDiscI()}
        # self._info = {**self._info, **self.getNetI()}
        # self._info = {**self._info, **self.getSensI()}


    @classmethod
    def _toPrint(self): #prints info
        print(self._info)
        self._info = {}

    @classmethod
    def _ret(self): #prints info
        return (self._info)
        self._info = {}


class SneToString(Sne): #prints info as string
    @classmethod
    def _PrintToString(self):
        print(str(self._info))
