import matplotlib.pyplot as plt
import setup

areaRecession           = None
lineOrange              = None
lineOrangeDash          = None
lineOrangeThin          = None
linePurple              = None
linePurpleTransparent   = None
linePurpleThin          = None
linePurpleLight         = None
linePurpleMedium        = None
linePink                = None
linePinkThin            = None
linePinkDash            = None
linePinkLight           = None
linePinkMedium          = None
lineGrayLight           = None
lineGrayMedium          = None
lineGrayMediumThin      = None
lineGrayDark            = None
lineGrayDarkThin        = None
lineBlack               = None
lineBlackThin           = None
xaxis                   = None

# Function to create properties
#def create_property(obj):
#    return obj
def run():
    global areaRecession, lineOrange, lineOrangeDash, lineOrangeThin, linePurple
    global linePurpleTransparent, linePurpleThin, linePurpleLight, linePurpleMedium, linePink
    global linePinkThin, linePinkDash, linePinkLight, linePinkMedium, lineGrayLight
    global lineGrayMediumm, lineGrayMediumThin, lineGrayDark, lineGrayDarkThin, lineBlack
    global lineBlackThin
    global xaxis

    # Set default properties for figures
    widthFigure     = 10
    heightFigure    = 5.625
    plt.rcParams['figure.figsize'] = (widthFigure, heightFigure)
    plt.rcParams['figure.dpi'] = 100
    #plt.rcParams['font.family'] = 'Helvetica'
    plt.rcParams['font.size'] = 15
    plt.rcParams['axes.labelsize'] = 15
    plt.rcParams['axes.titlesize'] = 15
    plt.rcParams['axes.titleweight'] = 'normal'
    plt.rcParams['xtick.color'] = 'black'
    plt.rcParams['ytick.color'] = 'black'
    plt.rcParams['grid.color'] = 'black'
    plt.rcParams['axes.linewidth'] = 0.8
    plt.rcParams['axes.grid'] = True
    plt.rcParams['axes.grid.axis'] = 'y'
    plt.rcParams['xtick.direction'] = 'out'
    plt.rcParams['ytick.direction'] = 'out'
    plt.rcParams['xtick.major.size'] = 0.005
    plt.rcParams['ytick.major.size'] = 0.005
    plt.rcParams['grid.linestyle'] = 'none'

    # Predefine color palette
    orange          = '#d95f02'
    purple          = '#59539d'
    purpleStandard  = '#7570b3'
    purpleLight     = '#bcbddc'
    purpleMedium    = '#9e9ac8'
    pink            = '#e7298a'
    pinkLight       = '#c994c7'
    pinkMedium      = '#df65b0'
    grayLight       = '#bdbdbd'
    grayMedium      = '#737373'
    grayDark        = '#252525'

    # Predefine area properties
    areaRecession = ({
        'facecolor': 'black',
        'linestyle': 'none',
        'alpha': 0.1
    })

    # Predefine line properties
    lineOrange = ({
        'color': orange,
        'linewidth': 2.4,
        'linestyle': '-'
    })

    lineOrangeDash = ({
        'color': orange,
        'linewidth': 2.4,
        'linestyle': '-.'
    })

    lineOrangeThin = ({
        'color': orange,
        'linewidth': 0.8,
        'linestyle': '-'
    })

    linePurple = ({
        'color': purple,
        'linewidth': 2.4
    })

    linePurpleTransparent = ({
        'color': purple,
        'linewidth': 2.4,
        'alpha': 0.5
    })

    linePurpleThin = ({
        'color': purple,
        'linewidth': 1.2
    })

    linePurpleLight = ({
        'color': purpleLight,
        'linewidth': 2.4
    })

    linePurpleMedium = ({
        'color': purpleMedium,
        'linewidth': 2.4
    })

    linePink = ({
        'color': pink,
        'linewidth': 2.4
    })

    linePinkThin = ({
        'color': pink,
        'linewidth': 1.2,
        'linestyle': '-.'
    })

    linePinkDash = ({
        'color': pinkLight,
        'linewidth': 2.4,
        'linestyle': '-.'
    })

    linePinkLight = ({
        'color': pinkLight,
        'linewidth': 2.4
    })

    linePinkMedium = ({
        'color': pinkMedium,
        'linewidth': 2.4
    })

    lineGrayLight = ({
        'color': grayLight,
        'linewidth': 2.4,
        'linestyle': '-.'
    })

    lineGrayMedium = ({
        'color': grayMedium,
        'linewidth': 2.4,
        'linestyle': '-.'
    })

    lineGrayMediumThin = ({
        'color': grayMedium,
        'linewidth': 0.8,
        'linestyle': '-.'
    })

    lineGrayDark = ({
        'color': grayDark,
        'linewidth': 2.4,
        'linestyle': '-.'
    })

    lineGrayDarkThin = ({
        'color': grayDark,
        'linewidth': 0.8,
        'linestyle': '-.'
    })

    lineBlack = ({
        'color': 'k',
        'linewidth': 2.4,
        'linestyle': '-'
    })

    lineBlackThin = ({
        'color': 'k',
        'linewidth': 0.8,
        'linestyle': '-'
    })

    # Predefine axis properties
    xaxis = ({
        'xlim': [setup.startDate, setup.endDate],
        'xticks': [1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
    })

