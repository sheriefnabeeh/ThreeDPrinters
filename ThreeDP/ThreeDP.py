
class ThreeDPs:

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
#             : cost_machineOperation = PrinterCapacity x Kw_Price x OperatingHrs_Per_Part
#             : cost_postProcessingPerBuild = 0 for now
#             : cost_ProcessingPerPart = material_raw_product_price_gram x weight_product
#             : cost_operatorPerHour
#             : cost_heatTreatmentPerBuild = 0 for now
#             : cost_postProcessingPerPart = 0 for now
#             : Time_part = time_build + OperatingHrs_Per_Part = time_production_perPart (with respect to weight_product)

    def __calculateCostOfProcessingPerPart(self) -> int:
        return self._material_raw_product_price_gram * (self._depreciation_percentage * self._mass_material + self._mass_material)
        
    def __calculateCostSingleProduct(self) -> int:
        return (self.__calculateCostOfProcessingPerPart() + (self._printerCapacity * self._cost_KW * self._time_build) +
                 self._cost_operatorPerHour + self._cost_postProcessingPerBuild + self._cost_heatTreatmentPerBuild +
                 self._cost_postProcessingPerPart)

    def updateTotalCost(self):
        self.total_cost = self._numberOfPartsProduced * self.__calculateCostSingleProduct()

    def updateTotalTime(self):
        self.total_time = (self._numberOfPartsProduced * self._time_build) / self._size_machines

    def __init__(self, data):
            self.demand_in_no_parts = int(data["demand_in_no_parts"])
            self._mass_material = int(data["weight_material_part"])
            self._size_machines = int(data["NumberOf3DPs"])
            self._time_build = int(data["OperatingHrs_Per_Part"])
            self._depreciation_percentage = float(data["depreciation_percentage"])
            self._cost_preProcessingPerPart = int(data["cost_preProcessingPerPart"])
            self._printerCapacity = float(data["printerCapacity"])
            self._cost_processingPerPart = float(data["cost_processingPerPart"])
            self._cost_operatorPerHour = float(data["cost_operatorPerHour"])
            self._cost_postProcessingPerBuild = float(data["cost_postProcessingPerBuild"])
            self._cost_heatTreatmentPerBuild = float(data["cost_heatTreatmentPerBuild"])
            self._cost_postProcessingPerPart = float(data["cost_postProcessingPerPart"])
            self._cost_KW = float(data["Kw_price"])
            self._material_raw_product_price_gram = float(data["material_raw_product_price_gram"])

# demand_in_no_parts= 3
# NumberOf3DPs= 1
# weight_material_part=3
# OperatingHrs_Per_Part=0
# time_build=0
# cost_preProcessingPerPart=0
# printerCapacity=0
# Kw_price=0
# material_raw_product_price_gram= 20
# cost_operatorPerHour=0
# cost_processingPerPart=0
# cost_postProcessingPerBuild=0
# cost_heatTreatmentPerBuild=0
# cost_postProcessingPerPart=0  