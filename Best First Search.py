from queue import PriorityQueue
def best_first_search(graph, start, goal, heuristic):
    queue = PriorityQueue()
    queue.put((heuristic[start], start))  
    visited = set()  
    while not queue.empty():
        _, current = queue.get()  
       
        if current == goal:
            return True 
       
        visited.add(current)  
       
        for neighbor in graph[current]:
            if neighbor not in visited:
                priority = heuristic[neighbor]  
                queue.put((priority, neighbor))  
       
    return False  

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

heuristic = {
    'A': 10,
    'B': 5,
    'C': 8,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 6
}
start_node = 'A'
goal_node = 'F'

result = best_first_search(graph, start_node, goal_node, heuristic)

if result:
    print("Goal reached!")
else:
    print("No solution found.")
