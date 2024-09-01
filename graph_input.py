import tkinter as tk
from tkinter import messagebox
import dfs_visualizer, bfs_visualizer

def submit_graph_data():
    n = int(entry_n.get())
    m = int(entry_m.get())

    if n <= 0 or m < 0:
        raise ValueError("Number of vertices must be positive, and number of edges cannot be negative.")

    adjacency_list = [[] for _ in range(n + 1)]

    for i in range(m):
        u = int(edge_entries[i][0].get())
        v = int(edge_entries[i][1].get())

        if not (1 <= u <= n) or not (1 <= v <= n):
            raise ValueError(f"Invalid input. Endpoints of every edge must be between 1 and {n}.")

        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    with open("graph_data.py", "w") as f:
        f.write(f"adjacency_list = {adjacency_list}\n")

    messagebox.showinfo("Success", "Graph saved!")
    
    tk.Button(root, text="Run DFS", command=dfs_visualizer.visualize_dfs).grid(row=5, column=0, padx=5, pady=5)
    tk.Button(root, text="Run BFS", command=create_bfs_source_entry_fields).grid(row=5, column=1, padx=5, pady=5)
    tk.Button(root, text="Exit", command=root.destroy).grid(row=5, column=2, padx=5, pady=5)

def create_edge_input_fields():
    m = int(entry_m.get())
    if m < 0:
        raise ValueError("Number of edges cannot be negative.")
    if m == 0:
        messagebox.showinfo("What are you doing?", "Enter a positive value as number of edges if you want to input edges!")
        return

    for widget in edge_frame.winfo_children():
        widget.destroy()
    edge_entries.clear()

    for i in range(m):
        label = tk.Label(edge_frame, text=f"Edge {i+1} (u, v):")
        label.grid(row=i, column=0, padx=5, pady=5)

        entry_u = tk.Entry(edge_frame, width=5)
        entry_u.grid(row=i, column=1, padx=5, pady=5)
        entry_v = tk.Entry(edge_frame, width=5)
        entry_v.grid(row=i, column=2, padx=5, pady=5)

        edge_entries.append((entry_u, entry_v))
        
def create_bfs_source_entry_fields():
    for widget in source_frame.winfo_children():
        widget.destroy()
        
    tk.Label(source_frame, text="Number of sources:").grid(row=0, column=0, padx=5, pady=5)
    entry_source_count = tk.Entry(source_frame, width=5)
    entry_source_count.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(source_frame, text="Input sources", command=lambda: get_sources(entry_source_count)).grid(row=0, column=2, padx=5, pady=5)
        
def get_sources(entry_source_count):
    source_count = int(entry_source_count.get())
    n = int(entry_n.get())
    if source_count < 0:
        raise ValueError("Number of sources cannot be negative")
    source_entries = []
    for i in range(source_count):
        label = tk.Label(source_frame, text=f"Source {i+1}:")
        label.grid(row=i+1, column=0, padx=5, pady=5)
        entry_source = tk.Entry(source_frame, width=5)
        entry_source.grid(row=i+1, column=1, padx=5, pady=5)
        source_entries.append(entry_source)
    
    tk.Button(source_frame, text="Go", command=lambda: process_sources(source_entries)).grid(row=source_count+1, column=0, columnspan=2, padx=5, pady=5)
    
def process_sources(source_entries):
    sources = []
    n = int(entry_n.get())
    for entry in source_entries:
        source = int(entry.get())
        if not (1 <= source <= n):
            raise ValueError(f"Invalid input. Each source must be between 1 and {n}")
        sources.append(int(entry.get()))
    with open("graph_data.py", "a") as f:
        f.write(f"sources = {sources}\n")
    bfs_visualizer.visualize_bfs()
    
        
def run_graph_input():
    global root, entry_n, entry_m, edge_frame, edge_entries, source_frame
    root = tk.Tk()
    root.title("Graph Input")

    tk.Label(root, text="Number of vertices (n):").grid(row=0, column=0, padx=5, pady=5)
    entry_n = tk.Entry(root)
    entry_n.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Number of edges (m):").grid(row=1, column=0, padx=5, pady=5)
    entry_m = tk.Entry(root)
    entry_m.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(root, text="Input edges", command=create_edge_input_fields).grid(row=2, column=1, padx=5, pady=5)

    edge_frame = tk.Frame(root)
    edge_frame.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    edge_entries = []
    
    source_frame = tk.Frame(root)
    source_frame.grid(row=6, column=1, padx=5, pady=5)

    tk.Button(root, text="Submit graph data", command=submit_graph_data).grid(row=4, column=1, padx=5, pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    run_graph_input()
