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

def main():
    file_path = Path(__file__).parent / "../inputs/day3.txt"
    answer = 0
    banks = get_input(file_path)
    for bank in banks:
        comb = 0
        joltages = [int(num) for num in bank]
        digit1, i1 = find_max(joltages[:-1])
        digit2 = max(joltages[1+i1:])
        comb = 10 * digit1 + digit2
        print(comb)
        answer += comb

    print("answer:", answer)
    # 3121910778619

if __name__ == '__main__':
    main()