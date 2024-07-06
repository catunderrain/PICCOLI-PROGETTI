def permute(sequence):
    def backtrack(start):
        if start == len(sequence):
            result.append(sequence[:])
            return

        for i in range(start, len(sequence)):
            sequence[start], sequence[i] = sequence[i], sequence[start]
            backtrack(start + 1)
            sequence[start], sequence[i] = sequence[i], sequence[start]

    result = []
    backtrack(0)
    return result


sequence = [1, 2, 3]
permutations = permute(sequence)

for perm in permutations:
    print(perm)