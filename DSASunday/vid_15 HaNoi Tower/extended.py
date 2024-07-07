import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

# Hàm vẽ cột và đĩa
def draw_tower(discs, ax):
    ax.clear()
    # Vẽ cột
    for i in range(5):
        ax.add_patch(patches.Rectangle((i * 5, 0), 0.2, 10, edgecolor='black', facecolor='black'))
    
    # Vẽ đĩa
    for i in range(len(discs)):
        for j in range(len(discs[i])):
            disc = discs[i][j]
            ax.add_patch(patches.Rectangle((i * 5 - disc / 3 + 0.1, j + 1), disc / 1.5, 0.5, edgecolor='black', facecolor='blue'))
    
    plt.xlim(-5, 25)
    plt.ylim(0, 10)
    plt.axis('off')
    plt.pause(0.2)

# Hàm di chuyển đĩa
def move_disc(discs, from_tower, to_tower):
    disc = discs[from_tower].pop()
    discs[to_tower].append(disc)

# Hàm tháp hà nội mở rộng
def thap_ha_noi_mo_rong(n, cot_nguon, cot_dich, cot_trung_gian_1, cot_trung_gian_2, cot_trung_gian_3, discs, ax):
    if n == 0:
        return
    if n == 1:
        move_disc(discs, cot_nguon, cot_dich)
        draw_tower(discs, ax)
        return
    k = n - 1
    thap_ha_noi_mo_rong(k, cot_nguon, cot_trung_gian_1, cot_trung_gian_2, cot_trung_gian_3, cot_dich, discs, ax)
    thap_ha_noi_mo_rong(n - k, cot_nguon, cot_dich, cot_trung_gian_3, cot_trung_gian_2, cot_trung_gian_1, discs, ax)
    thap_ha_noi_mo_rong(k, cot_trung_gian_1, cot_dich, cot_nguon, cot_trung_gian_2, cot_trung_gian_3, discs, ax)

# Thiết lập ban đầu
so_dia = 7
discs = [list(range(so_dia, 0, -1)), [], [], [], []]

# Khởi tạo đồ thị
fig, ax = plt.subplots()
draw_tower(discs, ax)

# Thực hiện thuật toán
thap_ha_noi_mo_rong(so_dia, 0, 4, 3, 2, 1, discs, ax)

plt.show()
