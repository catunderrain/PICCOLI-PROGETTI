import numpy as np
import matplotlib.pyplot as plt

GRID_SIZE = 263
grid = np.random.choice([0, 1], size=(GRID_SIZE, GRID_SIZE))

def update(grid):
    new_grid = grid.copy()
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            total = int((
                        grid[i, (j-1)%GRID_SIZE] + grid[i, (j+1)%GRID_SIZE] +
                        grid[(i-1)%GRID_SIZE, j] + grid[(i+1)%GRID_SIZE, j] +
                        grid[(i-1)%GRID_SIZE, (j-1)%GRID_SIZE] + grid[(i-1)%GRID_SIZE,(j+1)%GRID_SIZE] +
                        grid[(i+1)%GRID_SIZE, (j-1)%GRID_SIZE] + grid[(i+1)%GRID_SIZE, (j+1)%GRID_SIZE]
                        ))
            
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = 0
            else:   
                if total == 3:
                    new_grid[i, j] = 1

    return new_grid

for i in range(10000):  # Lưu 100 khung hình
    grid = update(grid)
    plt.imsave(rf"C:\Users\Lenovo\Desktop\PICCOLI PROGETTI\Conway's Game of Life\Pics\{i}.png", grid)
    print(f'Save img no.{i}')
