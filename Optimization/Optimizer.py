
# Initial objective function is : Minimize {Time + Cost}

# Constraints  : Cost < Cost_InjectionMoulding OR < Cost_Importing
#             : Time < Time_Importing/Injection
#             : Cost = demand x Cost_singleProduct
#             : Time = (demand x Time_part) / NumberOf3DPs
#             : Cost_singleProduct = cost_ProcessingPerPart + cost_machineOperation + cost_operatorPerHour
#                 + cost_postProcessingPerBuild + cost_heatTreatmentPerBuild + cost_postProcessingPerPart
#             : cost_machineOperation = PrinterCapacity x cost_power_KW x OperatingTime_Per_Part
#             : cost_postProcessingPerBuild = 0 for now
#             : cost_ProcessingPerPart = material_raw_product_price_gram/g x weight_product
#             : cost_operatorPerHour
#             : cost_heatTreatmentPerBuild = 0 for now
#             : cost_postProcessingPerPart = 0 for now
#             : Time_part = time_build + OperatingTime_Per_Part = time_production_perPart (with respect to weight_product)
#             : Time_operation = 1/3 Day // neglect for now
#             : NumberOf3DPs = number of threeDP available in cairo


from pulp import LpProblem, LpStatus, lpSum, LpVariable, LpMaximize

class Optimizer:
    
    def __init__(self) -> None:    
        
        model = LpProblem(name="NoOfProducts-Problem", sense=LpMaximize)
        demand = LpVariable(name="noOfProductsToBe3DPrinted", lowBound=0)
        cost = LpVariable(name="totalCost", lowBound=0)
        time = LpVariable(name="timeConsumed", lowBound=0)

        model += ( cost <= 1000, "cost_Importing_constraint")
        model += ( time <= 60, "time_Importing_constraint")
        model += ( cost == 10*demand, "cost_demand_constraint")
        model += ( time == 10/3*demand, "time_demand_constraint")
        model += lpSum([demand])        
        
        status = model.solve()
        
        print(f"status: {model.status}, {LpStatus[model.status]}")
        
        print(f"objective: {model.objective.value()}")
        
        for var in model.variables():
            print(f"{var.name}: {var.value()}")
            
        for name, constraint in model.constraints.items():
            print(f"{name}: {constraint.value()}")