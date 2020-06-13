# Functions to analyze ASIM Data
from datetime import *
import numpy as np


class ASIM:

    def __init__(self, name):
        self.name = name

    def datetimeLocationArray(self):
        data = []
        f = open(self.name, 'r')
        next(f)
        for line in f:
            temp = line.split(' ')
            day = temp[0].split('-')
            times = temp[1].split(':')
            hour = times[0]
            mins = times[1]
            secs = times[2].split('.')
            sec = secs[0]
            milli = secs[1].split('+')
            ms = milli[0]
            loc = line.replace(' ', '').split(',')
            lat = loc[1]
            lon = loc[2]
            datetimeEvent = datetime(int(day[0]),
                                  int(day[1]),
                                  int(day[2]),
                                  int(hour),
                                  int(mins),
                                  int(sec),
                                  int(ms))
            info = [datetimeEvent, lat, lon]
            data.append(info)
        f.close()
        return np.array(data)

