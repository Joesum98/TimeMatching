from datetime import *
from ASIM import ASIM
from TASD19 import TASD19
import numpy as np
import glob
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# geolocator = Nominatim(user_agent="TGF_Time_Matching")
timeDiff = timedelta(seconds=1)
TASDData = np.array([])
ASIMData = np.array([[]]).reshape(0, 3)
events = []
matches = []
TASDLocation = (39.29693, 112.90875)
pathTASD = 'C:/Users/JoeSum98/Documents/Code/Python/PycharmProjects/TimeMatching/Data/TASDData/**/*.dat'
pathASIM = 'C:/Users/JoeSum98/Documents/Code/Python/PycharmProjects/TimeMatching/Data/ASIMData/**/*.txt'


# returns true if two datetime objects are withing timedelta of one another
def similarTime(a: datetime, b: datetime, t: timedelta):
    d = a - b
    if abs(d) <= t:
        return True
    else:
        return False


# Takes an array and outputs a numpy array of burst events
def getBursts(array):
    data = []
    diff = np.diff(np.array(array))
    for index in range(0, len(diff)):
        if diff[index] <= timedelta(milliseconds=1):
            burst = True
            startIndex = index
            while burst:
                index = index + 1
                if diff[index] > timedelta(milliseconds=1):
                    burst = False
                    for j in range(startIndex, index + 1):
                        data.append(array[j])
    return np.array(data)


# Returns the distance between the ASIM event and the TASD
def distanceToTASD(event):
    location = (event[1][1], event[1][2])
    return geodesic(location, TASDLocation).km


for file in glob.glob(pathTASD, recursive=True):
    TASDData = np.concatenate((TASDData, TASD19.datetimeArray(TASD19(file))))

for file in glob.glob(pathASIM, recursive=True):
    ASIMData = np.concatenate((ASIMData, ASIM.datetimeLocationArray(ASIM(file))))

TASDbursts = getBursts(TASDData)

# Get Time Matched Data and store in "events"
for m in TASDbursts:
    for n in ASIMData:
        if similarTime(m, n[0], timeDiff):
            events.append([m, n])


f = open('MatchedTimes.txt', 'w')
f.write('TASD')
for i in range(0, 6):
    f.write('\t')
f.write('ASIM')
f.write('\n')
for match in events:
    f.write(match[0].strftime("%m/%d/%Y, %H:%M:%S.%f"))
    f.write('\t\t')
    f.write(match[1][0].strftime("%m/%d/%Y, %H:%M:%S.%f"))
    f.write('\n')
    f.write("Time Difference: " + str(abs(match[1][0] - match[0]).microseconds) + " microseconds")
    f.write("\nDistance to TASD: " + str(distanceToTASD(match)) + " kilometers")
    f.write('\n\n')
f.close()
