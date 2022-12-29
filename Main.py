import Optimization.Optimizer
import Utilities.InputGenerator
import Utilities.FileLoader
import Utilities.JsonParser
import ThreeDP.ThreeDP


def main():
    fileLoaderObject = Utilities.FileLoader.FileLoader("Variables_Definitions.txt")
    threeDPrinterData = fileLoaderObject.fetch()

    threeDPrinter =  ThreeDP.ThreeDP.ThreeDPs(threeDPrinterData) 
    threeDPrinter.updateTotalCost()    
    
    print("Program Finished")


if __name__ == "__main__":
    main()