
class InjectionMouldingClass:

    # Variable definitions :
    _price_of_stamba = 0
    _demand_if_range_not_used = 0
    _OperatingTime_Per_stamba = 0
    _depreciation_percentage = 0
    _cost_machineOperation = 0
    _cost_operatorPerHour = 0
    _cost_power_KW = 0
    _power_consumption = 0
    total_cost = 0
    total_time = 0
    _OperatingTime_StambaCreation = 0

    def __calculateCostOfProcessing(self) -> int:
        return (self._power_consumption * self._cost_power_KW * self._OperatingTime_Per_stamba) + self._cost_operatorPerHour * self._OperatingTime_Per_stamba

    def updateTotalCost(self):
        self.total_cost = self._price_of_stamba +  self._demand_if_range_not_used * self.__calculateCostOfProcessing()
        return self.total_cost
    
    def updateTotalTime(self):
        self.total_time = self._OperatingTime_StambaCreation + (self._demand_if_range_not_used * self._OperatingTime_Per_stamba)
        return self.total_time

    def useAndCheckCorrectnessOfTheVariableOnXAxis(self, variableChanged, value):
        successValue = value
        if(str(variableChanged).capitalize().find("PartsProduced")):
            self._demand_if_range_not_used = value
        elif(str(variableChanged).capitalize().find("material_raw_product")):
            self._price_of_stamba = value
        elif(str(variableChanged).capitalize().find("cost_power_KW")):
            self._cost_KW = value
        else:
            print("stop 3akk bro, variable in Range_To_loop_on has a spelling mistake" + 
                  "Options are PartsProduced, processingPerPart, material_raw_product, cost_power_KW")
            value = -1
        return value
    
    def __init__(self, data):
            self._price_of_stamba = int(data["price_of_stamba"])
            self._demand_if_range_not_used = int(data["demand_if_range_not_used"])
            self._OperatingTime_Per_stamba = int(data["OperatingTime_Per_stamba"])
            self._depreciation_percentage = float(data["depreciation_percentage"])
            self._cost_operatorPerHour = float(data["cost_operatorPerHour"])
            self._cost_power_KW = float(data["cost_power_KW"])
            self._power_consumption = float(data["power_consumption"])
            self._OperatingTime_StambaCreation = int(data["OperatingTime_StambaCreation"])

