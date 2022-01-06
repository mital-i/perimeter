import sys

sys.setrecursionlimit(10**6)

n = int(input())
graph = []

for i in range(102): 
    '''    line = []
    for j in range(30): 
        line[j] = '.' '''
    line = ['.']*102
    graph.append(line)
    
for i in range(n): 
    x, y = [int(i) for i in input().split()]
    graph[x][y] = "#"


def perimeter(graph): 
    peri = 0
    def flood_fill(x, y, graph, visited, length): 
        nonlocal peri
        #print(x, y, 'peri', peri)
        if((x,y) in visited):
            return
        
        visited.add((x, y))
        for (xx, yy) in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]: 
            if (xx, yy) not in visited and 0<=xx<102 and 0<=yy<102: 
                if graph[xx][yy] == '#': 
                    peri+=1
                else: 
                    flood_fill(xx, yy, graph, visited, length)
        
    flood_fill(0, 0, graph, set(()), 0)
    return peri
    
print(perimeter(graph))
