import numpy as np

def vogel_approximation_method(supply, demand, cost_matrix):
    supply = np.array(supply, dtype=int)
    demand = np.array(demand, dtype=int)
    cost_matrix = np.array(cost_matrix, dtype=int)
    
    n_rows, n_cols = cost_matrix.shape
    allocation = np.zeros((n_rows, n_cols), dtype=int)
    
    while np.any(supply > 0) and np.any(demand > 0):
        penalties = []
        
        # Calculate row penalties
        for i in range(n_rows):
            if supply[i] > 0:
                row_costs = [cost_matrix[i][j] for j in range(n_cols) if demand[j] > 0]
                if len(row_costs) > 1:
                    row_sorted = sorted(row_costs)
                    penalty = row_sorted[1] - row_sorted[0]
                    penalties.append((penalty, 'row', i))
                elif len(row_costs) == 1:
                    penalties.append((0, 'row', i))
        
        # Calculate column penalties
        for j in range(n_cols):
            if demand[j] > 0:
                col_costs = [cost_matrix[i][j] for i in range(n_rows) if supply[i] > 0]
                if len(col_costs) > 1:
                    col_sorted = sorted(col_costs)
                    penalty = col_sorted[1] - col_sorted[0]
                    penalties.append((penalty, 'col', j))
                elif len(col_costs) == 1:
                    penalties.append((0, 'col', j))
        
        if not penalties:
            break
        
        # Find the maximum penalty
        max_penalty = max(penalties, key=lambda x: x[0])
        
        if max_penalty[1] == 'row':
            i = max_penalty[2]
            available_demand = [(j, cost_matrix[i][j]) for j in range(n_cols) if demand[j] > 0]
            min_cost_demand = min(available_demand, key=lambda x: x[1])[0]
        else:
            j = max_penalty[2]
            available_supply = [(i, cost_matrix[i][j]) for i in range(n_rows) if supply[i] > 0]
            min_cost_supply = min(available_supply, key=lambda x: x[1])[0]
        
        # Allocate as much as possible
        if max_penalty[1] == 'row':
            j = min_cost_demand
            allocation_amount = min(supply[i], demand[j])
            allocation[i][j] = allocation_amount
            supply[i] -= allocation_amount
            demand[j] -= allocation_amount
        else:
            i = min_cost_supply
            allocation_amount = min(supply[i], demand[j])
            allocation[i][j] = allocation_amount
            supply[i] -= allocation_amount
            demand[j] -= allocation_amount
    
    return allocation

# Example usage:
supply = [50, 60, 50]
demand = [30, 40, 50, 40]
cost_matrix = [
    [3, 1, 7, 4],
    [2, 6, 5, 9],
    [8, 3, 3, 2]
]

allocation = vogel_approximation_method(supply, demand, cost_matrix)
print("Allocation Matrix:")
print(allocation)
