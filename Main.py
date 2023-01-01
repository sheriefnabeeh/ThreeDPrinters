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
    
    optimizer = Optimization.Optimizer.Optimizer()
    print(optimizer)


if __name__ == "__main__":
    main()