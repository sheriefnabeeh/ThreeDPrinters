
class ThreeDPs:

    # Variable definitions :
    _numberOfPartsProduced = 0
    _mass_material = 0
    _time_build = 0
    _cost_depreciation = 0
    _cost_preProcessingPerPart = 0
    _cost_machineOperation = 0
    _cost_materialPerG = 0
    _cost_processingPerPart = 0
    _cost_operatorPerHour = 0
    _cost_postProcessingPerBuild = 0
    _cost_heatTreatmentPerBuild = 0
    _cost_postProcessingPerPart = 0
    _size_machines = 0
    _cost_KW = 0
    _material_raw_product_price_gram = 0
    total_cost = 0

# exposed functionality :
    def updateTotalCost(self):
        self.total_cost = self._mass_material + self._cost_preProcessingPerPart

    def __init__(self, data):
            self.demand_in_no_parts = data["demand_in_no_parts"]
            self._mass_material = data["weight_material_part"]
            self._size_machines = data["Size_3DPs"]
            self._time_build = data["OperatingHrs_Per_Part"]
            self._cost_depreciation = data["cost_depreciation"]
            self._cost_preProcessingPerPart = data["cost_preProcessingPerPart"]
            self._cost_machineOperation = data["printerCapacity"]
            self._cost_materialPerG = data["cost_materialPerG"]
            self._cost_processingPerPart = data["cost_processingPerPart"]
            self._cost_operatorPerHour = data["cost_operatorPerHour"]
            self._cost_postProcessingPerBuild = data["cost_postProcessingPerBuild"]
            self._cost_heatTreatmentPerBuild = data["cost_heatTreatmentPerBuild"]
            self._cost_postProcessingPerPart = data["cost_postProcessingPerPart"]
            self._cost_KW = data["Kw_price"]
            self._material_raw_product_price_gram = data["material_raw_product_price_gram"]
#demand_in_no_parts= 3
# Size_3DPs = 1
# weight_material_part=3
# OperatingHrs_Per_Part=0
# time_build=0
# cost_depreciation=0
# cost_preProcessingPerPart=0
# printerCapacity=0
# Kw_price =0
# material_raw_product_price_gram = 20
# cost_materialPerG=0
# cost_operatorPerHour=0
# cost_processingPerPart=0
# cost_operatorPerHour=0
# cost_postProcessingPerBuild=0
# cost_heatTreatmentPerBuild=0
# cost_postProcessingPerPart=0  