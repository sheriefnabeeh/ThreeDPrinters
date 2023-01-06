import Optimization.Optimizer
import Utilities.InputGenerator
import Utilities.FileLoader as utils
import Utilities.JsonParser
import ThreeDP.ThreeDP as printer
import Utilities.Plotting as plotty

def main():
    fileLoaderObject = utils.FileLoader("Variables_Definitions.txt")
    dataFetched = fileLoaderObject.fetch()

    threeDPrinter =  printer.ThreeDPs(dataFetched) 
    threeDPrinter.updateTotalCost()    
    
    
    drawer = plotty.Drawer(dataFetched)
    drawer.draw()


if __name__ == "__main__":
    main()