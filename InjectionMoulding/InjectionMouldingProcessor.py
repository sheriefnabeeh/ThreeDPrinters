
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
    
    def __calculateCostOfProcessing(self) -> int:
        return self._material_raw_product_price_gram * (self._depreciation_percentage * self._mass_material + self._mass_material)
        

    
    def updateTotalCost(self):
        self.total_cost = self._numberOfPartsProduced * self.__calculateCostSingleProduct()
        return self.total_cost
    
    def updateTotalTime(self):
        self.total_time = (self._numberOfPartsProduced * self._time_build) / self._size_machines
        return self.total_time

    def __init__(self, data):
            self._price_of_stamba = int(data["price_of_stamba"])
            self._demand_if_range_not_used = int(data["demand_if_range_not_used"])
            self._OperatingTime_Per_stamba = int(data["OperatingTime_Per_stamba"])
            self._depreciation_percentage = int(data["depreciation_percentage"])
            self._cost_machineOperation = float(data["cost_machineOperation"])
            self._cost_operatorPerHour = float(data["cost_operatorPerHour"])
            self._cost_power_KW = float(data["cost_power_KW"])
            self._power_consumption = float(data["power_consumption"])
