n = int(input())
graph = []
for i in range(10): 
    line = []
    for j in range(10): 
        line.append('.')
    graph.append(line)
    
for i in range(n): 
    x, y = [int(i) for i in input().split()]
    graph[x][y] = "#"
    
print(graph)

def perimeter(graph): 
    peri = None
    def flood_fill(x, y, graph, stack, visited, length): 
        nonlocal peri
        visited.add((x, y))
        graph[x][y]='O'
        if peri: 
            return 
        if len(stack)==0: 
            peri = length[0]
            return 
        for (xx, yy) in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]: 
            if (xx, yy) not in visited and 0<xx<=10 and 0<yy<=10: 
                if graph[xx][yy] == '#': 
                    length[0]+=1
                else: 
                    flood_fill(xx, yy, graph, stack, visited, length)
        
    flood_fill(0, 0, graph, [], set(()), [0])
    return peri
    
print(perimeter(graph))
