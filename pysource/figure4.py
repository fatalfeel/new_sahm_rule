import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages

import setup
import getRecession
import getUnemployment
import getVacancy
import createIndicatorCountercyclical
import createIndicatorProcyclical

def run():
    startRecession, endRecession = getRecession.run()
    u = getUnemployment.run()
    v = getVacancy.run()

    # Compute unemployment, vacancy, and minimum indicators
    uIndicator      = createIndicatorCountercyclical.run(u, setup.meanWindow, setup.minWindow)
    vIndicator      = createIndicatorProcyclical.run(v, setup.meanWindow, setup.minWindow)
    minIndicator    = np.minimum(uIndicator, vIndicator)

    for t, m in zip(setup.timeline, minIndicator):
        print(f"{t}, {m}")

    df = pd.DataFrame({'Time': setup.timeline,'Indicator': minIndicator})
    df.to_csv(setup.outputFolder+'newsahm_pascal.csv', index=False)

    # Plotting with matplotlib
    pdf = PdfPages(setup.outputFolder+'newsahm_pascal.pdf')

    plt.figure(figsize=(12, 6))
    plt.title('New Sahm Rule by Pascal')
    plt.plot(setup.timeline, minIndicator, label='Minimum Indicator', color='blue')
    plt.xticks(np.arange(1920, 2030, 10))
    plt.ylim(bottom=0.000)

    tickX       = plt.gca().get_xticks()
    tickyear    = np.append(tickX, int(setup.timeline[-1]))
    plt.xticks(tickyear)

    # Change color of the last tick label
    tick_labels = plt.gca().get_xticklabels()
    for i, label in enumerate(tick_labels):
        if i < len(tick_labels)-1:  # Last label
            label.set_color('black')  # Set others to black (or any color you prefer)
        else:
            label.set_color('red')  # Change its color to red

    tickY       = plt.gca().get_yticks()
    tick3pp     = np.append(tickY, 0.003)
    tick8pp     = np.append(tickY, 0.008)
    combined_ticks = np.unique(np.append(tick3pp, tick8pp))
    plt.yticks(combined_ticks)
    plt.axhline(y=0.003, color='r', linestyle=':', linewidth=2)
    plt.axhline(y=0.008, color='r', linestyle=':', linewidth=2)

    xlimit = plt.gca().get_xlim()[1] + 1.0
    plt.text(xlimit,
             0.003,
             'trigger',
             color='red',
             fontsize=10,
             verticalalignment='center')  # Positioning next to the 0.003 y-tick

    plt.text(xlimit,
             0.008,
             'crisis',
             color='red',
             fontsize=10,
             verticalalignment='center')  # Positioning next to the 0.008 y-tick

    for start, end in zip(startRecession, endRecession):
        plt.axvspan(start, end, color='grey', alpha=0.8)

    plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(1))
    plt.gca().tick_params(axis='both',  which='major', length=10, width=1, direction='out', labelsize=8)
    plt.gca().tick_params(axis='x',     which='minor', length=5,  width=1, direction='out')

    pdf.savefig()
    pdf.close()

    plt.show()
