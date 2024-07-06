def permute(sequence):
    if len(sequence) == 1:
        return [sequence]

    permutations = []

    for i in range(len(sequence)):
        current = sequence[i]
        remaining = sequence[:i] + sequence[i+1:]

        for perm in permute(remaining):
            permutations.append([current] + perm)

    return permutations

# Dãy số ban đầu
sequence = [1, 2, 3,4,5]

# Tạo tất cả các hoán vị
permutations = permute(sequence)

# In kết quả
for perm in permutations:
    print(perm)
