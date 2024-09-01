import importlib
from graph_visualizer import get_visualization
from collections import deque

INF = 10**9

def bfs(adjacency_list, sources):
    
    n = len(adjacency_list) - 1
    d = [INF]*(n+1)
    queue = deque(sources)
    for s in sources:
        d[s] = 0
    
    while queue:
        u = queue.popleft()
        canvas.itemconfig(ovals[u], fill='green')
        canvas.update()
        root.after(1000)
        for v in adjacency_list[u]:
            if d[v] == INF:
                d[v] = d[u] + 1
                queue.append(v)
    
def visualize_bfs():
    import graph_data
    importlib.reload(graph_data)
    from graph_data import adjacency_list, sources
    global root, canvas, ovals
    root, canvas, ovals = get_visualization(adjacency_list)
    bfs(adjacency_list, sources)  
    root.mainloop() 
    
if __name__ == "__main__":
    visualize_bfs()
    