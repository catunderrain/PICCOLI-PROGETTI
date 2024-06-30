import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Kích thước lưới
GRID_SIZE = 100

# Định nghĩa hướng di chuyển của con kiến (bắt đầu hướng lên)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Lên, phải, xuống, trái

# Khởi tạo lưới ban đầu và con kiến
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
ant_position = (GRID_SIZE // 2, GRID_SIZE // 2)  # Vị trí ban đầu của con kiến
ant_direction = 0  # Hướng ban đầu của con kiến

# Hàm cập nhật trạng thái mới của lưới và vị trí của con kiến
def update(frameNum, img, grid, ant_position, ant_direction):
    # Lấy giá trị ô hiện tại của con kiến
    ant_x, ant_y = ant_position
    current_value = grid[ant_x, ant_y]
    
    # Thay đổi giá trị ô
    grid[ant_x, ant_y] = 1 - current_value  # Đảo giá trị của ô
    
    # Xác định hướng mới của con kiến dựa trên giá trị ô hiện tại
    if current_value == 0:  # Nếu ô trống, con kiến quay sang trái 90 độ
        ant_direction = (ant_direction - 1) % 4
    else:  # Nếu ô đã được đánh dấu, con kiến quay sang phải 90 độ
        ant_direction = (ant_direction + 1) % 4
    
    # Di chuyển con kiến sang phía trước
    delta_x, delta_y = directions[ant_direction]
    ant_x = (ant_x + delta_x) % GRID_SIZE
    ant_y = (ant_y + delta_y) % GRID_SIZE
    ant_position = (ant_x, ant_y)
    
    # Cập nhật hình ảnh lưới
    img.set_array(grid)
    return img,

# Khởi tạo hình ảnh ban đầu của lưới
fig, ax = plt.subplots()
img = ax.imshow(grid, cmap='binary', interpolation='nearest')

# Tạo animation
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, ant_position, ant_direction),
                              frames=10000, interval=10, blit=True)

plt.title("Mô phỏng Langton's Ant")
plt.show()
