import numpy as np
import pandas as pd
from datetime import datetime

inputFolder     = None
outputFolder    = None
startDate       = None
endDate         = None
timeline        = None
iFigure         = None
meanWindow      = None
minWindow       = None
lowThreshold    = None
highThreshold   = None
sahmThreshold   = None

def run():
    global inputFolder, outputFolder, timeline, iFigure
    global meanWindow, minWindow, lowThreshold, highThreshold, sahmThreshold
    global startDate, endDate, timeline
    #plt.close('all')
    #sys.modules.clear()

    # Set paths to input and output folders
    inputFolder     = '../raw/'
    outputFolder    = '../figures/'

    # Set analysis dates
    startDate   = 1929.25
    # endDate     = 2024 + 7/12 #year + (month-1)/12
    cvsdata     = pd.read_csv(inputFolder + 'UNEMPLOY.csv', header=None)
    lastrow     = datetime.strptime(cvsdata.iloc[-1][0], "%Y-%m-%d")
    endDate     = lastrow.year + (lastrow.month-1)/12

    timeline    = np.arange(startDate, endDate + 1/12, 1/12)
    timeline    = np.round(timeline, 4)

    # Reset figure counter
    iFigure     = 0

    # Set window for trailing average (in months)
    meanWindow  = 3

    # Set window for minimum (in months)
    minWindow   = 12

    # Set thresholds
    lowThreshold    = 0.003
    highThreshold   = 0.008
    sahmThreshold   = 0.005
