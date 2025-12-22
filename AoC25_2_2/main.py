from pathlib import Path
import math

def get_ranges(file_path) -> list:
    with open(file_path) as f:
        ranges = (f.readline()).split(',')
    return ranges

def id_check(start, end) -> int:
    ans = 0
    for num in range(start, end+1):
        num = str(num)
        if num[0] != 0:
            seqs = []
            for i in range(1, len(num)):
                seqs.append(num[:i])
            for seq in seqs:
                print(seqs)
                print(len(num) / len(seq))
                if math.remainder(len(num), len(seq)) == 0.0:
                    ans += int(seq)

    return ans

def main():
    file_path = Path(__file__).parent / "../inputs/test.txt"
    ranges = get_ranges(file_path)
    solution = 0
    for distance in ranges:
        start = int((distance.split('-'))[0])
        end = int((distance.split('-'))[1])
        solution += id_check(start, end)

    print(f"answer: {solution}")

# 4174379265 <- expected

if __name__ == "__main__":
    main()