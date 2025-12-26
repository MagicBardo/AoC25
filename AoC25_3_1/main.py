from pathlib import Path

def get_input(file_path) -> list:
    with open(file_path, 'r') as f:
        lines = [s.strip("\n") for s in f.readlines()]
    return lines

def main():
    file_path = Path(__file__).parent / "../inputs/test.txt"
    solution = 0
    banks = get_input(file_path)
    greatest_sums = []
    print(banks)
    for bank in banks:
        pos_sum = []
        for joltage in bank:
            for i in range(len(bank)):
                if bank[i] != joltage:
                    pos_sum.append(joltage + bank[i])
        print(max(pos_sum))
        greatest_sums.append(max(pos_sum))

    for greatest_sum in greatest_sums:
        print(greatest_sum)

    print("answer:", solution)

if __name__ == '__main__':
    main()