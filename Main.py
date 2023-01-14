import Utilities.InputGenerator
import Utilities.FileLoader as utils
import Utilities.JsonParser
import ThreeDP.ThreeDP as printerModule

import Utilities.Plotting as plotty

FILE_NAME = "Variables_Definitions.txt"
JSONFILE_NAME = "Variables_Definitions.json"

STH_WENT_WRONG = -1

def main():
#    fileReaderTool = utils.FileLoader(FILE_NAME)
    jsonReaderTool = utils.FileLoader(JSONFILE_NAME)

#    data_that_Tota_has_entered = fileReaderTool.fetchDataFromFile()
    data_that_Tota_has_entered_in_Json = jsonReaderTool.fetchDataFromJsonFile()

    toBePrintedParts = []
    specificationsForPart = data_that_Tota_has_entered_in_Json['3DPrinted_Products']
    for part in specificationsForPart:
         toBePrintedParts.append(printerModule.ThreeDPrinterObject(part))
            
#    threeDPrinter = printerModule.ThreeDPrinterObject(data_that_Tota_has_entered)

    x_axis_values_from_txtFile = plotty.createListOfValuesToLoopOn(data_that_Tota_has_entered_in_Json["type_of_data_to_be_generated"], int(
        data_that_Tota_has_entered_in_Json["beginningValueFor_X_axis"]), int(data_that_Tota_has_entered_in_Json["endingValueFor_X_axis"]), int(data_that_Tota_has_entered_in_Json["step_in_range"]))

    xAxisVariable = data_that_Tota_has_entered_in_Json["x_axis_variable"]
    plottingData = [[],[], []]

    for dataValue in x_axis_values_from_txtFile:
        if (toBePrintedParts[0].useAndCheckCorrectnessOfTheVariableOnXAxis(xAxisVariable, dataValue) == STH_WENT_WRONG ):
            print("variable or value passed in the txt file has sth wrong.")
            break

        cost = toBePrintedParts[0].updateTotalCost()
        time = toBePrintedParts[0].updateTotalTime()
        plottingData[0].append(dataValue)
        plottingData[1].append(cost)
        plottingData[2].append(time)

    drawer = plotty.Drawer(data_that_Tota_has_entered_in_Json["plotTitle"])
    drawer.setPlot_X_and_Y_Names(str(xAxisVariable), "cost", "time")
    drawer.draw(plottingData)


if __name__ == "__main__":
    main()
