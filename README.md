# TimeMatching
Match times of ASIM data and TASD data


Create one folder for all of the TASD data and one for all the ASIM data.
Set "pathTASD" and "pathASIM" to their respective paths (I have "/**/*.txt" appened to mine as I have multiple folders separating years of data). /**
TASD data should be .dat files and ASIM data should be .txt.
Set "timeDiff" to a timedelta of the opening time you are interested in.

Formatting starts on line 67.
TASD data is stored in a 1-D numpy array with datetime objects in each entry.
ASIM data is stored in a 2-D, 3xN numpy array; each entry has [0] = DataTime object, [1] = latitude, [2] = longitutde.


Note:
    geolocator not used yet. 
