import Optimization.Optimizer
import Utilities.InputGenerator
import Utilities.FileLoader as utils
import Utilities.JsonParser
import ThreeDP.ThreeDP as printer
import Utilities.Plotting as plotty


def main():
    fileLoaderObject = utils.FileLoader("Variables_Definitions.txt")
    dataFetched = fileLoaderObject.fetch()

    threeDPrinter = printer.ThreeDPs(dataFetched)

    listOfValuesPassed = plotty.generateData(dataFetched["range_type"], int(
        dataFetched["beginning_range"]), int(dataFetched["end_range"]), int(dataFetched["step_in_range"]))

    xAxisVariable = dataFetched["Range_variable_to_loop_on"]
    plottingData = [[],[], []]

    for dataValue in listOfValuesPassed:
        if (threeDPrinter.updateVarianceForPlotting(xAxisVariable, dataValue) == -1 ):
            print("faulty data")
            break

        cost = threeDPrinter.updateTotalCost()
        time = threeDPrinter.updateTotalTime()
        plottingData[0].append(dataValue)
        plottingData[1].append(cost)
        plottingData[2].append(time)

    drawer = plotty.Drawer(dataFetched["plotTitle"])
    drawer.setGraphVariables(str(xAxisVariable), "cost", "time")
    drawer.draw(plottingData)


if __name__ == "__main__":
    main()
