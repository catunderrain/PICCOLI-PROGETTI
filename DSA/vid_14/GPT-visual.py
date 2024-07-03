import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

# Hàm vẽ cột và đĩa
def draw_tower(discs, ax):
    ax.clear()
    # Vẽ cột
    for i in range(3):
        ax.add_patch(patches.Rectangle((i * 5, 0), 0.2, 10, edgecolor='black', facecolor='black'))
    
    # Vẽ đĩa
    for i in range(len(discs)):
        for j in range(len(discs[i])):
            disc = discs[i][j]
            ax.add_patch(patches.Rectangle((i * 5 - disc / 2 + 0.1, j + 1), disc, 0.5, edgecolor='black', facecolor='blue'))
    
    plt.xlim(-5, 15)
    plt.ylim(0, 10)
    plt.axis('off')
    plt.pause(0.5)

# Hàm di chuyển đĩa
def move_disc(discs, from_tower, to_tower):
    disc = discs[from_tower].pop()
    discs[to_tower].append(disc)

# Hàm tháp hà nội
def thap_ha_noi(n, cot_nguon, cot_dich, cot_trung_gian, discs, ax):
    if n == 1:
        move_disc(discs, cot_nguon, cot_dich)
        draw_tower(discs, ax)
        return
    thap_ha_noi(n - 1, cot_nguon, cot_trung_gian, cot_dich, discs, ax)
    move_disc(discs, cot_nguon, cot_dich)
    draw_tower(discs, ax)
    thap_ha_noi(n - 1, cot_trung_gian, cot_dich, cot_nguon, discs, ax)

# Thiết lập ban đầu
so_dia = 5
discs = [list(range(so_dia, 0, -1)), [], []]

# Khởi tạo đồ thị
fig, ax = plt.subplots()
draw_tower(discs, ax)

# Thực hiện thuật toán
thap_ha_noi(so_dia, 0, 2, 1, discs, ax)

plt.show()
