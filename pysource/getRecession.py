import pandas as pd
import setup

def run():
    # Read month numbers for recession start and end dates
    #A22: A36
    #startTable  = pd.read_csv(setup.inputFolder + '20210719_cycle_dates_pasted.csv', usecols=[0], skiprows=20, nrows=15)
    # read to last line
    startTable  = pd.read_csv(setup.inputFolder + '20210719_cycle_dates_pasted.csv', usecols=[0], skiprows=20)

    #B22:B36
    #endTable    = pd.read_csv(setup.inputFolder + '20210719_cycle_dates_pasted.csv', usecols=[1], skiprows=20, nrows=15)
    # read to last line
    endTable    = pd.read_csv(setup.inputFolder + '20210719_cycle_dates_pasted.csv', usecols=[1], skiprows=20)

    # Transform table into datetime array
    # Convert the start and end dates into datetime arrays
    start_array = pd.to_datetime(startTable.iloc[:, 0]) + pd.DateOffset(months=1)  # Add one month
    end_array   = pd.to_datetime(endTable.iloc[:, 0])

    # Translate dates into year + fraction of year
    start_recession = start_array.dt.year + (start_array.dt.month - 1) / 12
    end_recession = end_array.dt.year + (end_array.dt.month - 1) / 12

    return start_recession.to_numpy(), end_recession.to_numpy()

