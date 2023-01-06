# This module here is required for Plotting the demand_in_no_parts against the Cost and Time :

# once in a 3D manner where demand_in_no_parts, Cost and time are represented.
# once in the 2D representation of the same plot.

# The main Point we need :
#   Plot the cost/demand_in_no_parts until we find the point where
#   the cost hits the cost of a commercially printed object

from enum import Enum
import matplotlib.pyplot as plt
import numpy as np


def generateData(type, beginning, limit, step):
    if str(type).capitalize().find("RANGE"):
        return np.arange(beginning, limit, step).tolist()
    elif str(type).capitalize().find("RANDOM_INT"):
        return np.random.randint(beginning, limit)
    elif str(type).capitalize().find("RANDOM"):
        return np.random.rand(beginning, limit)

class Drawer:

    _xLabel = "x - axis"
    _yLabel = "y - axis"
    _line1Label = "line 1"
    _line2Label = "line 1"
    _plotTitle = "Two lines on same graph"
    _x_Data = [1, 2, 3]
    _y_Data = [1, 4, 1]
    _y2_Data = [4, 4, 2]

    def __init__(self, data):

        self._xLabel = data["xlabel"]
        self._yLabel = data["ylabel"]
        self._line1Label = data["line1label"]
        self._line2Label = data["line2label"] or "line 2"
        self._plotTitle = data["plotTitle"]
        self._x_Data = data["x_Data"] or []
        self._y_Data = data["y_Data"] or []
        self._y2_Data = data["y2_Data"] or []
        
        # ax1.tick_params(axis='y', labelcolor=color)
    
    def draw(self) -> None:
        color = 'tab:red'
        fig, firstAxis = plt.subplots()
        # naming the x axis
        firstAxis.set_xlabel(self._xLabel)
        # naming the y axis
        firstAxis.set_ylabel(self._yLabel, color=color)
        # giving a title to my graph
        firstAxis.set_title(self._plotTitle)
        # line 1 points
        x1 = self._x_Data
        y1 = self._y_Data
        # plotting the line 1 points 

        firstAxis.plot(x1, y1, label=self._line1Label, color=color)

        if (self._y2_Data):
            secondAxis = firstAxis.twinx()
            # line 2 points
            y2 = self._y2_Data

            color = 'tab:blue'
            secondAxis.set_ylabel(self._yLabel, color=color)
            # plotting the line 2 points 
            secondAxis.plot(x1, y2, label=self._line2Label)

        # show a legend on the plot
        plt.legend()
        plt.grid('true')
        # function to show the plot
        fig.tight_layout()
        plt.savefig("mygraph.png")
