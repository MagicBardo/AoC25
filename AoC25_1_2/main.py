def get_file_input(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    return lines

def get_rotation_amount(line):
    line = line.strip()
    rotation_amount = int(line[1:])
    return rotation_amount

def main():
    file_path = "./input1.txt"
    dial_info = {
        "positions": 100,
        "min": 0,
        "max": 99,
        "start": 50
    }
    zero_pos_count = 0
    curr_pos = dial_info["start"]
    coefficient = 0
    max_crossed = False
    min_crossed = False

    lines = get_file_input(file_path)
    for line in lines:
        if line.startswith("R"):
            rot_am = get_rotation_amount(line)

            if curr_pos < dial_info["max"] < curr_pos + rot_am:
                coefficient = (curr_pos + rot_am) // dial_info["positions"]
                max_crossed = True
            curr_pos = (curr_pos + rot_am) % dial_info["positions"]
        elif line.startswith("L"):
            rot_am = get_rotation_amount(line)

            if curr_pos > dial_info["min"] > curr_pos - rot_am:
                coefficient = (curr_pos - rot_am) // -dial_info["positions"]
                min_crossed = True

            curr_pos = (curr_pos - rot_am + 100) % dial_info["positions"]
        else:
            raise "Unexpected line: Couldn't find 'R' or 'L'!"

        if curr_pos == 0:
            zero_pos_count += 1
            if max_crossed and coefficient != 1:
                zero_pos_count += coefficient
            elif min_crossed and coefficient != 1:
                zero_pos_count += coefficient
        elif max_crossed and coefficient != 1:
            zero_pos_count += coefficient
        elif min_crossed and coefficient != 1:
            zero_pos_count += coefficient

    print("Code: {}".format(zero_pos_count))


if __name__ == '__main__':
    main()
