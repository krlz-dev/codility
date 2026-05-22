def solution(N):
    binary_value = bin(N)[2:]
    gaps = binary_value.strip("0").split("1")
    print(gaps)
    max_gap = max(len(gap) for gap in gaps)
    return max_gap

print(solution(778581))