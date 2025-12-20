def get_ranges(file_path:str) -> list:
    with open(file_path) as f:
        line:str = f.readline()
        ranges = line.split(',')
    return ranges

def id_check(start:int, end:int) -> int:
    ans = 0
    for num in range(start, end+1):
        num = str(num)
        for seq_len in range(0, len(num)):
            seq = num[seq_len]
            if num.count(seq) == 2:
                pass

    return ans

def main():
    file_path:str = "./AoC25_2_1/input.txt"
    ranges:list = get_ranges(file_path)
    for range in ranges:
        start:int = int((range.split('-'))[0])
        end:int = int((range.split('-'))[1])
        solutions = id_check(start, end)

    print(f"Answer: {ans}")


if __name__ == "__main__":
    main()