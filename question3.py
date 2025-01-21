from scipy.optimize import linprog #pip install scipy

c = [-20,-30]

 #objective function - 20 chairs and 30 tables
 #since the package uses minimization technique we turn maximization to minimisation

A = [
    [1, 5],
    [3, 1]
]             
#has all the constraints

b = [125, 80]
#constants of constraints

#bounds for variables
x_bounds = (0, None)
y_bounds = (0, None)

result = linprog(c, A_ub = A, b_ub = b, bounds= [x_bounds, y_bounds], method= 'highs')
#solve the problem with linprog


#check the success?
if result.success:
    chairs = result.x[0]
    tables = result.x[1]
    
    max_profit = -result.fun 
    #convert to positive from minimization
    print(f"Optimal number of chairs: {chairs}")
    print(f"OPtimal number of tables: {tables}")
    print(f"Maximum amount of profit: ${max_profit}")
else:
    print("No solution.")