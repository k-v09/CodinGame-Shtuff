def find_neighbors(grid):
    height = len(grid)
    width = len(grid[0])
    nodes = []

    for y in range(height):
        for x in range(width):
            if grid[y][x] == '0':
                nodes.append((x, y))

    results = []
    for node_x, node_y in nodes:
        
        right_x, right_y = -1, -1
        for x in range(node_x + 1, width):
            if grid[node_y][x] == '0':
                right_x, right_y = x, node_y
                break

        bottom_x, bottom_y = -1, -1
        for y in range(node_y + 1, height):
            if grid[y][node_x] == '0':
                bottom_x, bottom_y = node_x, y
                break

        results.append((node_x, node_y, right_x, right_y, bottom_x, bottom_y))

    return results

width = int(input())
height = int(input())
grid = [input().strip() for _ in range(height)]

neighbors = find_neighbors(grid)
for node in neighbors:
    print(*node)