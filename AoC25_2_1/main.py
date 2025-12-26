from pathlib import Path

def get_ranges(file_path) -> list:
    with open(file_path) as f:
        ranges = (f.readline()).split(',')
    return ranges

def id_check(start, end) -> int:
    ans = 0
    for num in range(start, end+1):
        num = str(num)
        if num[0] != 0 and len(num) % 2 == 0:
            seq = num[:len(num) // 2]
            if num.count(seq) == 2:
                ans += int(num)
    return ans

def main():
    file_path = Path(__file__).parent / "../inputs/day2.txt"
    ranges = get_ranges(file_path)
    solution = 0
    for distance in ranges:
        start = int((distance.split('-'))[0])
        end = int((distance.split('-'))[1])
        solution += id_check(start, end)

    print(f"answer: {solution}")

if __name__ == "__main__":
    main()