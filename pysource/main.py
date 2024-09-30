'''
download the 3 lastest cvs files to ../raw and run
https://fred.stlouisfed.org/series/CLF16OV
https://fred.stlouisfed.org/series/JTSJOL
https://fred.stlouisfed.org/series/UNEMPLOY
'''

import os
import setup
import formatFigure
import figure4

# Set parameters
if __name__ == '__main__':
    currentPath = os.getcwd()
    if 'pysource' not in currentPath:
        os.chdir(os.getcwd()+'/pysource')

    setup.run()
    formatFigure.run()
    figure4.run()
