import numpy as np
import pandas as pd

def run(v, meanWindow, minWindow):
    # Compute trailing average
    v_series = pd.Series(v)

    # Compute the trailing (moving) average
    '''In Python with pandas, the rolling(window=meanWindow) function already behaves similarly, 
       as it considers the current value and meanWindow - 1 previous values.'''
    vMean = v_series.rolling(window=meanWindow, min_periods=1).mean()

    # Compute the trailing (moving) maximum
    vMax = vMean.rolling(window=minWindow+1, min_periods=1).max()

    # Compute exact indicator
    vIndicatorExact = vMax - vMean

    # Round the exact indicator to 4 decimal places
    vIndicator = np.round(vIndicatorExact, 4)

    return vIndicator

