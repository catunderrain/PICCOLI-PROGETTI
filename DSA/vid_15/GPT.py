def thap_ha_noi(n, cot_nguon, cot_dich, cot_trung_gian):
    if n == 1:
        print(f"Di chuyển đĩa 1 từ cột {cot_nguon} sang cột {cot_dich}")
        return
    thap_ha_noi(n - 1, cot_nguon, cot_trung_gian, cot_dich)
    print(f"Di chuyển đĩa {n} từ cột {cot_nguon} sang cột {cot_dich}")
    thap_ha_noi(n - 1, cot_trung_gian, cot_dich, cot_nguon)

so_dia = 3
print(thap_ha_noi(so_dia, 'A', 'C', 'B'))
