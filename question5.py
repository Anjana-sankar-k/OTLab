from scipy.optimize import linprog #pip install scipy

c = [-5,-3]

A = [
    [2, 1],
    [1, 1]
]             

b =[500, 400]
#constants of constraints

#bounds for variables
x_bounds = (100, None)
y_bounds = (50, None)

result = linprog(c, A_ub = A, b_ub = b, bounds= [x_bounds, y_bounds], method= 'highs')
#solve the problem with linprog


#check the success?
if result.success:
    chocolate = result.x[0]
    vanilla = result.x[1]
    
    max_profit = -result.fun 
    #convert to positive from minimization
    print(f"Optimal number of chairs: {chocolate}")
    print(f"OPtimal number of tables: {vanilla}")
    print(f"Maximum amount of profit: ${max_profit}")
else:
    print("No solution.")