import math

def calculate_eoq(demand, ordering_cost, holding_cost):
    return math.sqrt((2*demand*ordering_cost)/holding_cost)

annual_demand = 10000
ordering_cost = 200
holding_cost = 5

eoq = calculate_eoq(annual_demand, ordering_cost, holding_cost)

print(f"The economic order quantity (EOQ) is {eoq: .2f}")
