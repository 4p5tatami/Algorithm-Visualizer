import importlib
from graph_visualizer import get_visualization

def dfs(u, canvas, ovals, vis, adj):
    vis[u] = 1
    canvas.itemconfig(ovals[u], fill='cyan')
    canvas.update()
    root.after(1000) 
    for v in adj[u]:
        if vis[v] == 1: continue
        dfs(v, canvas, ovals, vis, adj)
    canvas.itemconfig(ovals[u], fill='green')
    canvas.update()
    root.after(1000)

def visualize_dfs():
    import graph_data
    importlib.reload(graph_data)
    from graph_data import adjacency_list
    n = len(adjacency_list) - 1
    vis = [0] * (n + 1)
    global root, canvas, ovals
    root, canvas, ovals = get_visualization(adjacency_list)

    for i in range(1, n + 1):
        if vis[i] == 0:
            dfs(i, canvas, ovals, vis, adjacency_list)
    root.mainloop()

if __name__ == "__main__":
    visualize_dfs()
