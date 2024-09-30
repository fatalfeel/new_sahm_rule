import numpy as np
import pandas as pd
import setup

def run():

    # Get vacancy rate for 1929M4–1950M12
    #D477: D737
    vRate1929 = pd.read_csv(setup.inputFolder + 'HistoricalSeries_JME_2020January.csv', usecols=[3], skiprows=475, nrows=261).values.flatten() / 100

    # Get vacancy rate for 1951M1–2000M12
    #C9: C608
    vRate1951 = pd.read_csv( setup.inputFolder + 'CompositeHWI.xlsx - Sheet1.csv', usecols=[2], skiprows=7, nrows=600).values.flatten() / 100

    # Get vacancy rate for 2001M1–2024M7
    # Read vacancy level
    #B2: B285
    #vLevel2001 = pd.read_csv( setup.inputFolder + 'JTSJOL.csv', usecols=[1], skiprows=0, nrows=284).values.flatten()
    # read to last line
    vLevel2001 = pd.read_csv(setup.inputFolder + 'JTSJOL.csv', usecols=[1], skiprows=0).values.flatten()

    # Read labor-force level
    #B638:B921
    #laborforce = pd.read_csv( setup.inputFolder + 'CLF16OV.csv', usecols=[1], skiprows=636, nrows=284).values.flatten()
    # read to last line
    laborforce = pd.read_csv(setup.inputFolder + 'CLF16OV.csv', usecols=[1], skiprows=636).values.flatten()

    # Compute vacancy rate
    vRate2001 = vLevel2001 / laborforce

    # Splice three series into a long series
    v = np.concatenate((vRate1929, vRate1951, vRate2001))

    return v

