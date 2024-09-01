import tkinter as tk
import math

def draw_graph(adjacency_list):
    radius = 20
    width, height = 600, 600

    n = len(adjacency_list) - 1
    node_positions, ovals = [None]*(n+1), [None]*(n+1)

    for i in range(1, n+1):
        angle = 2 * math.pi * (n-i) / n
        x = width // 2 + int(math.cos(angle) * (width // 3))
        y = height // 2 + int(math.sin(angle) * (height // 3))
        node_positions[i] = (x, y)
        ovals[i] = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="white")
        canvas.create_text(x, y, text=str(i))

    for u in range(1, n+1):
        for v in adjacency_list[u]:
            x1, y1 = node_positions[u] 
            x2, y2 = node_positions[v]
            dx, dy = x2 - x1, y2 - y1
            dist = math.sqrt(dx*dx + dy*dy)
            if dist == 0:
                continue

            dx /= dist
            dy /= dist

            x1 += dx * radius
            y1 += dy * radius
            x2 -= dx * radius
            y2 -= dy * radius

            canvas.create_line(x1, y1, x2, y2)
    
    return ovals
        

def get_visualization(adjacency_list):
    global canvas
    root = tk.Tk()
    root.title("Graph")

    canvas = tk.Canvas(root, width=600, height=600, bg="white")
    canvas.pack()

    ovals = draw_graph(adjacency_list)  # Draw the graph here
    return root, canvas, ovals

if __name__ == "__main__":
    get_visualization()