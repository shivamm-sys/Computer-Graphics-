# Function to draw a line using Bresenham Algorithm
def bresenham_line(x1, y1, x2, y2):
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1
    err = dx - dy

    x, y = x1, y1
    while True:
        points.append((x, y))
        if x == x2 and y == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
    return points


# Function to draw a polygon by connecting given vertices
def draw_polygon(vertices):
    all_points = []
    n = len(vertices)
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  
        line_points = bresenham_line(x1, y1, x2, y2)
        all_points.extend(line_points)
    return all_points


n = int(input("Enter number of sides of polygon: "))
vertices = []

print("Enter coordinates (x y) of each vertex:")
for i in range(n):
    x, y = map(int, input(f"Vertex {i+1}: ").split())
    vertices.append((x, y))

# Draw the polygon
polygon_points = draw_polygon(vertices)

print("\nPoints generated for the polygon:")
for p in polygon_points:
    print(p)
