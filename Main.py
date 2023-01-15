import Utilities.InputGenerator
import Utilities.FileLoader as utils
import Utilities.JsonParser
import ThreeDP.ThreeDP as printerModule
import InjectionMoulding.InjectionMouldingProcessor as MouldingModule
import Utilities.Plotting as plotty

JSONFILE_NAME = "Variables_Definitions.json"

STH_WENT_WRONG = -1

def main():

    jsonReaderTool = utils.FileLoader(JSONFILE_NAME)

#    data_that_Tota_has_entered = fileReaderTool.fetchDataFromFile()
    data_that_Tota_has_entered_in_Json = jsonReaderTool.fetchDataFromJsonFile()

    listOfSpecificationFor3DPrinteredParts = []
    listOfSpecificationForInjectionMouldingParts = []

    for part in data_that_Tota_has_entered_in_Json['3DPrinted_Products']:
         listOfSpecificationFor3DPrinteredParts.append(printerModule.ThreeDPrinterObject(part))

    for part in data_that_Tota_has_entered_in_Json['InjectionMoulding_Products']:
         listOfSpecificationForInjectionMouldingParts.append(MouldingModule.InjectionMouldingClass(part))

            
    x_axis_values_from_txtFile = plotty.createListOfValuesToLoopOn(data_that_Tota_has_entered_in_Json["type_of_data_to_be_generated"], int(
        data_that_Tota_has_entered_in_Json["beginningValueFor_X_axis"]), int(data_that_Tota_has_entered_in_Json["endingValueFor_X_axis"]), int(data_that_Tota_has_entered_in_Json["step_in_range"]))

    xAxisVariable = data_that_Tota_has_entered_in_Json["x_axis_variable"]
    
    plottingData3DP = [[],[], []]
    plottingDataInjectionMoulding = [[],[], []]
    
    for dataValue in x_axis_values_from_txtFile:
        if (listOfSpecificationFor3DPrinteredParts[0].useAndCheckCorrectnessOfTheVariableOnXAxis(xAxisVariable, dataValue) == STH_WENT_WRONG ):
            print("variable or value passed in the txt file has sth wrong.")
            break

        cost = listOfSpecificationFor3DPrinteredParts[0].updateTotalCost()
        time = listOfSpecificationFor3DPrinteredParts[0].updateTotalTime()
        plottingData3DP[0].append(dataValue)
        plottingData3DP[1].append(cost)
        plottingData3DP[2].append(time)
        
        if (listOfSpecificationForInjectionMouldingParts[0].useAndCheckCorrectnessOfTheVariableOnXAxis(xAxisVariable, dataValue) == STH_WENT_WRONG ):
            print("variable or value passed in the txt file has sth wrong.")
            break
        cost = listOfSpecificationForInjectionMouldingParts[0].updateTotalCost()
        time = listOfSpecificationForInjectionMouldingParts[0].updateTotalTime()
        plottingDataInjectionMoulding[0].append(dataValue)
        plottingDataInjectionMoulding[1].append(cost)
        plottingDataInjectionMoulding[2].append(time)

    drawer = plotty.Drawer(data_that_Tota_has_entered_in_Json["plotTitle"])
    drawer.setPlot_X_and_Y_Names(str(xAxisVariable), "cost", "time")
    drawer.set_X_Data(plottingData3DP[0])
    drawer.append_Y1_Data(plottingData3DP[1])
    drawer.append_Y2_Data(plottingData3DP[2])

    drawer.append_Y1_Data(plottingDataInjectionMoulding[1])
    drawer.append_Y2_Data(plottingDataInjectionMoulding[2])


    drawer.draw()
if __name__ == "__main__":
    main()
