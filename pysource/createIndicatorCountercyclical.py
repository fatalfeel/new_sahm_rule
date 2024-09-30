import numpy as np
import pandas as pd

def run(u, meanWindow, minWindow):
    # Compute trailing average
    u_series = pd.Series(u)

    # Compute the trailing (moving) average
    '''In Python with pandas, the rolling(window=meanWindow) function already behaves similarly, 
       as it considers the current value and meanWindow - 1 previous values.'''
    uMean = u_series.rolling(window=meanWindow, min_periods=1).mean()

    # Compute the trailing (moving) minimum
    uMin = uMean.rolling(window=minWindow+1, min_periods=1).min()

    # Compute exact indicator
    uIndicatorExact = uMean - uMin

    # Round the exact indicator to 4 decimal places
    uIndicator = np.round(uIndicatorExact, 4)

    return uIndicator
