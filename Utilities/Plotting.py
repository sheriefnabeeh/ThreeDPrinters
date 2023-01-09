# This module here is required for Plotting the demand_if_range_not_used against the Cost and Time :

# once in a 3D manner where demand_if_range_not_used, Cost and time are represented.
# once in the 2D representation of the same plot.

# The main Point we need :
#   Plot the cost/demand_if_range_not_used until we find the point where
#   the cost hits the cost of a commercially printed object

from enum import Enum
import matplotlib.pyplot as plt
import numpy as np


def createListOfValuesToLoopOn(type, beginning, limit, step):
    typeCleaned = str(type).strip().lower()
    if typeCleaned.__contains__("range"):
        print( "generating range")
        return np.arange(beginning, limit, step).tolist()
    elif typeCleaned.__contains__("random"):
        print( "generating random data")
        return np.random.random((limit)) * limit
    else:
        raise Exception("the following value passed and is not correct: " + typeCleaned)

class Drawer:

    _xLabel = "x - axis"
    _yLabel = "y - axis"
    _y2Label = "y2 - axis"
    _line1Label = "line 1"
    _line2Label = "line 2"
    _plotTitle = "Two lines on same graph"

    def setPlot_X_and_Y_Names(self, x_label, y_label, y2_label):
        self._xLabel = x_label
        self._yLabel = y_label
        self._y2Label = y2_label
        
    def __init__(self, title):
        self._plotTitle = title
    
    def draw(self, tupleData) -> None:
        
        color = 'tab:red'
        fig, firstAxis = plt.subplots()
        # naming the x axis
        firstAxis.set_xlabel(self._xLabel)
        # naming the y axis
        firstAxis.set_ylabel(self._yLabel, color=color)
        # giving a title to my graph
        firstAxis.set_title(self._plotTitle)
        
        x1 = tupleData[0]
        y1 = tupleData[1]

        firstAxis.plot(x1, y1, label=self._line1Label, color=color)
        firstAxis.tick_params(axis='y', labelcolor=color)

        if (tupleData[2]):
            secondAxis = firstAxis.twinx()
            # line 2 points
            y2 = tupleData[2]

            color = 'tab:blue'
            secondAxis.set_ylabel(self._y2Label, color=color)
            # plotting the line 2 points 
            secondAxis.plot(x1, y2, label=self._line2Label, color=color)
            secondAxis.tick_params(axis='y', labelcolor=color)
            
        plt.grid('true')
        # function to show the plot
        fig.tight_layout()
        plt.savefig("mygraph.png")
