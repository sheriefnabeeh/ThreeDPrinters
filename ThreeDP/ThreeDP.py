
class ThreeDPrinterObject:

    # Variable definitions :
    _numberOfPartsProduced = 0
    _mass_material = 0
    _time_build = 0
    _depreciation_percentage = 0
    _cost_preProcessingPerPart = 0
    _cost_machineOperation = 0
    _cost_processingPerPart = 0
    _cost_operatorPerHour = 0
    _cost_postProcessingPerBuild = 0
    _cost_heatTreatmentPerBuild = 0
    _cost_postProcessingPerPart = 0
    _size_machines = 0
    _cost_KW = 0
    _printerCapacity = 0
    _material_raw_product_price_gram = 0
    total_cost = 0
    total_time = 0
    
#             : Cost = demand x Cost_singleProduct
#             : Time = (demand x Time_part) / NumberOf3DPs
#             : Cost_singleProduct = cost_ProcessingPerPart + cost_machineOperation + cost_operatorPerHour
#                 + cost_postProcessingPerBuild + cost_heatTreatmentPerBuild + cost_postProcessingPerPart
#             : cost_machineOperation = PrinterCapacity x cost_power_KW x OperatingTime_Per_Part
#             : cost_postProcessingPerBuild = 0 for now
#             : cost_ProcessingPerPart = material_raw_product_price_gram x weight_product
#             : cost_operatorPerHour
#             : cost_heatTreatmentPerBuild = 0 for now
#             : cost_postProcessingPerPart = 0 for now
#             : Time_part = time_build + OperatingTime_Per_Part = time_production_perPart (with respect to weight_product)

    def __calculateCostOfMaterialPerPart(self) -> int:
        return self._material_raw_product_price_gram * (self._depreciation_percentage * self._mass_material + self._mass_material)
        
    def __calculateCostSingleProduct(self) -> int:
        return (self.__calculateCostOfMaterialPerPart() + (self._printerCapacity * self._cost_KW * self._time_build) +
                (self._cost_operatorPerHour * self._time_build) + self._cost_postProcessingPerBuild + self._cost_heatTreatmentPerBuild +
                self._cost_postProcessingPerPart)

    def useAndCheckCorrectnessOfTheVariableOnXAxis(self, variableChanged, value):
        successValue = value
        if(str(variableChanged).capitalize().find("PartsProduced")):
            self._numberOfPartsProduced = value
        elif(str(variableChanged).capitalize().find("material_raw_product")):
            self._material_raw_product_price_gram = value
        elif(str(variableChanged).capitalize().find("cost_power_KW")):
            self._cost_KW = value
        else:
            print("stop 3akk bro, variable in Range_To_loop_on has a spelling mistake" + 
                  "Options are PartsProduced, processingPerPart, material_raw_product, cost_power_KW")
            value = -1
        return value
    
    def updateTotalCost(self):
        self.total_cost = self._numberOfPartsProduced * self.__calculateCostSingleProduct()
        return self.total_cost
    
    def updateTotalTime(self):
        self.total_time = (self._numberOfPartsProduced * self._time_build) / self._size_machines
        return self.total_time

    def __init__(self, data):
            self.demand_if_range_not_used = int(data["demand_if_range_not_used"])
            self._mass_material = int(data["weight_of_product_after_production"])
            self._size_machines = int(data["NumberOf3DPs"])
            self._time_build = int(data["OperatingTime_Per_Part"])
            self._depreciation_percentage = float(data["depreciation_percentage"])
            self._cost_preProcessingPerPart = int(data["cost_preProcessingPerPart"])
            self._printerCapacity = float(data["printerCapacity"])
            self._cost_operatorPerHour = float(data["cost_operatorPerHour"])
            self._cost_postProcessingPerBuild = float(data["cost_postProcessingPerBuild"])
            self._cost_heatTreatmentPerBuild = float(data["cost_heatTreatmentPerBuild"])
            self._cost_postProcessingPerPart = float(data["cost_postProcessingPerPart"])
            self._cost_KW = float(data["cost_power_KW"])
            self._material_raw_product_price_gram = float(data["material_raw_product_price_gram"])
