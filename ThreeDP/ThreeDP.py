
class ThreeDPs:

    # Variable definitions :
    _numberOfPartsProduced = 0
    _mass_material = 0
    _time_setupBuild = 0
    _time_build = 0
    _cost_depreciation = 0
    _cost_preProcessingPerPart = 0
    _cost_machineOperation = 0
    _cost_materialPerKG = 0
    _cost_processingPerPart = 0
    _cost_operatorPerHour = 0
    _cost_postProcessingPerBuild = 0
    _cost_heatTreatmentPerBuild = 0
    _cost_postProcessingPerPart = 0

    total_cost = 0

# exposted functionality :
    def updateTotalCost(self):
        self.total_cost = self._mass_material + self._cost_preProcessingPerPart

    def __init__(self, numberOfPartsProduced,
                 mass_material,
                 time_setupBuild,
                 time_build,
                 cost_depreciation,
                 cost_preProcessingPerPart,
                 cost_machineOperation,
                 cost_materialPerKG,
                 cost_processingPerPart,
                 cost_operatorPerHour,
                 cost_postProcessingPerBuild,
                 cost_heatTreatmentPerBuild,
                 cost_postProcessingPerPart):
        self._numberOfPartsProduced = numberOfPartsProduced
        self._mass_material = mass_material
        self._time_setupBuild = time_setupBuild
        self._time_build = time_build
        self._cost_depreciation = cost_depreciation
        self._cost_preProcessingPerPart = cost_preProcessingPerPart
        self._cost_machineOperation = cost_machineOperation
        self._cost_materialPerKG = cost_materialPerKG
        self._cost_processingPerPart = cost_processingPerPart
        self._cost_operatorPerHour = cost_operatorPerHour
        self._cost_postProcessingPerBuild = cost_postProcessingPerBuild
        self._cost_heatTreatmentPerBuild = cost_heatTreatmentPerBuild
        self._cost_postProcessingPerPart = cost_postProcessingPerPart

    def __init__(self, data):
            self.numberOfPartsProduced = data["numberOfPartsProduced"]
            self._mass_material = data["mass_material"]
            self._time_setupBuild = data["time_setupBuild"]
            self._time_build = data["time_build"]
            self._cost_depreciation = data["cost_depreciation"]
            self._cost_preProcessingPerPart = data["cost_preProcessingPerPart"]
            self._cost_machineOperation = data["cost_machineOperation"]
            self._cost_materialPerKG = data["cost_materialPerKG"]
            self._cost_processingPerPart = data["cost_processingPerPart"]
            self._cost_operatorPerHour = data["cost_operatorPerHour"]
            self._cost_postProcessingPerBuild = data["cost_postProcessingPerBuild"]
            self._cost_heatTreatmentPerBuild = data["cost_heatTreatmentPerBuild"]
            self._cost_postProcessingPerPart = data["cost_postProcessingPerPart"]
