import Utilities.InputGenerator
import Utilities.FileLoader as utils
import Utilities.JsonParser
import ThreeDP.ThreeDP as printerModule

import Utilities.Plotting as plotty

FILE_NAME = "Variables_Definitions.txt"
STH_WENT_WRONG = -1

def main():
    fileReaderTool = utils.FileLoader(FILE_NAME)
    data_that_Tota_has_entered = fileReaderTool.fetchDataFromFile()

    threeDPrinter = printerModule.ThreeDPrinterObject(data_that_Tota_has_entered)

    x_axis_values_from_txtFile = plotty.createListOfValuesToLoopOn(data_that_Tota_has_entered["type_of_data_to_be_generated"], int(
        data_that_Tota_has_entered["beginningValueFor_X_axis"]), int(data_that_Tota_has_entered["endingValueFor_X_axis"]), int(data_that_Tota_has_entered["step_in_range"]))

    xAxisVariable = data_that_Tota_has_entered["x_axis_variable"]
    plottingData = [[],[], []]

    for dataValue in x_axis_values_from_txtFile:
        if (threeDPrinter.useAndCheckCorrectnessOfTheVariableOnXAxis(xAxisVariable, dataValue) == STH_WENT_WRONG ):
            print("variable or value passed in the txt file has sth wrong.")
            break

        cost = threeDPrinter.updateTotalCost()
        time = threeDPrinter.updateTotalTime()
        plottingData[0].append(dataValue)
        plottingData[1].append(cost)
        plottingData[2].append(time)

    drawer = plotty.Drawer(data_that_Tota_has_entered["plotTitle"])
    drawer.setPlot_X_and_Y_Names(str(xAxisVariable), "cost", "time")
    drawer.draw(plottingData)


if __name__ == "__main__":
    main()
