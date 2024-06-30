Thuật toán mà bạn đang đề cập đến có thể là một phần của "Trò chơi của sự sống" (Conway's Game of Life), một trò chơi mô phỏng sự sống được phát minh bởi nhà toán học John Conway vào năm 1970. Đây là một tự động hóa ô vuông (cellular automaton) được biết đến rộng rãi và nghiên cứu nhiều trong lĩnh vực lý thuyết trò chơi, hệ thống động lực học, và toán học.

Luật của Trò chơi của sự sống (Conway's Game of Life)
Tạo một lưới ô vuông hai chiều: Mỗi ô có thể ở một trong hai trạng thái: sống (sáng) hoặc chết (tắt).

Quy tắc chuyển trạng thái:

Sống sót: Một ô sống với 2 hoặc 3 ô hàng xóm sống sẽ tiếp tục sống.
Chết: Một ô sống với ít hơn 2 hoặc nhiều hơn 3 ô hàng xóm sống sẽ chết.
Sống lại: Một ô chết với đúng 3 ô hàng xóm sống sẽ trở thành sống.
Dưới đây là cách triển khai cơ bản của Trò chơi của sự sống trong Python:

Triển khai Trò chơi của sự sống trong Python
python
Sao chép mã
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Thiết lập kích thước lưới
GRID_SIZE = 50

# Tạo lưới ban đầu ngẫu nhiên
grid = np.random.choice([0, 1], size=(GRID_SIZE, GRID_SIZE))

def update(frameNum, img, grid):
    # Tạo một bản sao của lưới để tránh thay đổi lưới gốc trong khi đang cập nhật
    new_grid = grid.copy()
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            # Đếm số ô hàng xóm sống
            total = int((grid[i, (j-1)%GRID_SIZE] + grid[i, (j+1)%GRID_SIZE] +
                         grid[(i-1)%GRID_SIZE, j] + grid[(i+1)%GRID_SIZE, j] +
                         grid[(i-1)%GRID_SIZE, (j-1)%GRID_SIZE] + grid[(i-1)%GRID_SIZE, (j+1)%GRID_SIZE] +
                         grid[(i+1)%GRID_SIZE, (j-1)%GRID_SIZE] + grid[(i+1)%GRID_SIZE, (j+1)%GRID_SIZE]))
            
            # Áp dụng quy tắc của trò chơi
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1

    # Cập nhật lưới và hình ảnh
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,

# Tạo hình ảnh ban đầu
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')

# Tạo animation
ani = animation.FuncAnimation(fig, update, fargs=(img, grid), frames=10, interval=200, save_count=50)

plt.show()
Giải thích mã
Khởi tạo lưới:

GRID_SIZE: Kích thước của lưới (50x50).
grid: Lưới ban đầu được tạo ngẫu nhiên với các ô sống (1) hoặc chết (0).
Hàm update:

Tạo một bản sao của lưới để áp dụng các quy tắc mà không thay đổi lưới gốc ngay lập tức.
Đếm số ô hàng xóm sống của mỗi ô.
Áp dụng các quy tắc của Trò chơi của sự sống để cập nhật trạng thái của mỗi ô.
Cập nhật hình ảnh lưới để hiển thị.
Hàm animation.FuncAnimation:

Tạo animation để liên tục cập nhật và hiển thị lưới theo thời gian.
Kết quả
Chạy mã này sẽ hiển thị một lưới ô vuông, nơi các ô sống và chết thay đổi trạng thái theo quy tắc của Trò chơi của sự sống. Mỗi bước thời gian (frame) sẽ cập nhật trạng thái của lưới dựa trên trạng thái hiện tại của nó và các quy tắc được mô tả ở trên.