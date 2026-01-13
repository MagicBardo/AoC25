from pathlib import Path

def get_input(file_path) -> list:
    with open(file_path, 'r') as f:
        lines = [s.strip("\n") for s in f.readlines()]
    return lines

def find_max(joltages):
    max_value = 0
    max_index = 0
    for i, joltage in enumerate(joltages):
        if joltage > max_value:
            max_value = joltage
            max_index = i
    return  max_value, max_index

def final(bank, k):
    joltages = [int(num) for num in bank]
    N = len(joltages)
    offset = 0
    ans = 0
    for j in range(k):
        subjoltages = joltages[offset:N - (k - j - 1)]
        digit, max_i = find_max(subjoltages)
        offset += max_i + 1
        ans += digit * 10**(k - j - 1)
    return ans

def main():
    file_path = Path(__file__).parent / "../inputs/day3.txt"
    answer = 0
    banks = get_input(file_path)
    for bank in banks:
        answer += final(bank, 12)
    print("answer:", answer)

if __name__ == '__main__':
    main()