def get_ranges(file_path:str) -> list:
    with open(file_path) as f:
        line:str = f.readline()
        ranges = line.split(',')
    return ranges

def id_check(start:int, end:int) -> int:
    ans = 0


    return ans

def main():
    file_path:str = "./AoC25_2_1/input.txt"
    ranges:list = get_ranges(file_path)
    for distance in ranges:
        start:int = int((distance.split('-'))[0])
        end:int = int((distance.split('-'))[1])
        solutions:int = id_check(start, end)


if __name__ == "__main__":
    main()