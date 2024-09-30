import numpy as np
import pandas as pd
import setup

def run():
    # Get unemployment rate for 1929M4–1947M12
    #B477:B701
    uRate1929 = pd.read_csv(setup.inputFolder + 'HistoricalSeries_JME_2020January.csv', usecols=[1], skiprows=475, nrows=225).values.flatten() / 100

    # Get unemployment rate for 1948M1–2024M7
    # Read unemployment level
    #B2: B921
    #uLevel1948 = pd.read_csv(setup.inputFolder + 'UNEMPLOY.csv',    usecols=[1], skiprows=0, nrows=920).values.flatten()
    #read to last line
    uLevel1948 = pd.read_csv(setup.inputFolder + 'UNEMPLOY.csv', usecols=[1], skiprows=0).values.flatten()

    # Read monthly labor-force level
    #B2:B921
    #laborforce = pd.read_csv(setup.inputFolder + 'CLF16OV.csv',     usecols=[1], skiprows=0, nrows=920).values.flatten()
    # read to last line
    laborforce = pd.read_csv(setup.inputFolder + 'CLF16OV.csv', usecols=[1], skiprows=0).values.flatten()

    # Compute unemployment rate
    uRate1948 = uLevel1948 / laborforce

    # Splice two series into a long series
    u = np.concatenate((uRate1929, uRate1948))

    return u

