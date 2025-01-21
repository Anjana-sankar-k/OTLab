from scipy.optimize import linprog #pip install scipy

c = [-200,-150]

A = [
    [1, 1],
    [20, 10], 
    [10, 15]
]             

b =[60, 1200, 600]
#constants of constraints

#bounds for variables
x_bounds = (20, None)
y_bounds = (10, None)

result = linprog(c, A_ub = A, b_ub = b, bounds= [x_bounds, y_bounds], method= 'highs')
#solve the problem with linprog


#check the success?
if result.success:
    wheat = result.x[0]
    barley = result.x[1]
    
    max_profit = -result.fun 
    #convert to positive from minimization
    print(f"Optimal number of chairs: {wheat}")
    print(f"OPtimal number of tables: {barley}")
    print(f"Maximum amount of profit: ${max_profit}")
else:
    print("No solution.")