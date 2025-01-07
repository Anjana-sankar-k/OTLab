import math

def tsp(graph, visited, curr_city, cities_visited, total_cost, min_cost):
    if cities_visited == len(graph):
        return total_cost +graph[curr_city][0] if graph[curr_city][0] > 0 else math.inf
    
    for next_city in range(len(graph)):
        if not visited[next_city] and graph[curr_city][next_city] > 0:
            visited[next_city] = True
            min_cost = min(
                min_cost, 
                tsp(graph, visited, next_city, cities_visited + 1, total_cost +graph[curr_city][next_city], min_cost)
            )
            visited[next_city] = False
    return min_cost
            
def solve_tsp(graph):
    n = len(graph)
    visited = [False] * n 
    visited[0] = True
    return tsp(graph, visited, 0, 1, 0, math.inf)

total = int(input("Enter the total number of cities: "))
array = []

print("enter cost of travelling from i to j as arr[i][j]: ")
for i in range(total):
    row = list(map(int, input().split()))
    array.append(row)
        
print("The distance between cities: ")
for row in array:
    print(row)

result = solve_tsp(array)
print("Minimum cost of TSP is ", result if result != math.inf else "No solution found")



