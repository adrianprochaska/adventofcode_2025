# template for each days exercise file


def get_day() -> int:
    # find day number from filename
    import os

    filename = os.path.basename(__file__)
    day_str = filename.split("_")[0]
    return int(day_str)


def input_filename(test: bool) -> str:
    day = get_day()
    if test:
        return f"{day:02d}_test.txt"
    else:
        return f"{day:02d}_in.txt"


def find_max_digit(num_str, start_idx, end_idx, direction):
    max_digit = 0
    max_idx = start_idx
    for idx in range(start_idx, end_idx, direction):
        current_digit = int(num_str[idx])
        if current_digit >= max_digit:
            max_digit = current_digit
            max_idx = idx

    return max_digit, max_idx


def largest_joltage(num_str, jolt_size=2):
    start_idx = len(num_str) - 1
    step = -1
    end_idx = -1
    start_num = 0

    digit_ary = []
    left_idx = -1
    for n_loop in range(jolt_size):
        right_idx = len(num_str) - (jolt_size - n_loop)
        max_digit, left_idx = find_max_digit(num_str, right_idx, left_idx, -1)

        digit_ary.append(max_digit)

    joltage_output = 0
    ten_power = jolt_size
    for elm in digit_ary:
        ten_power -= 1
        joltage_output += elm * 10 ** (ten_power)

    return joltage_output


def run(part: int, test: bool):
    # part 1: sum of lines
    if part == 1:
        total = 0
        with open(input_filename(test)) as f:
            for line in f:
                total += largest_joltage(line.strip(), jolt_size=2)
        print(f"Part 1: The sum of all largest joltages is {total}")

    # part 2: product of lines
    elif part == 2:
        total = 0
        with open(input_filename(test)) as f:
            for line in f:
                total += largest_joltage(line.strip(), jolt_size=12)
        print(f"Part 2: The sum of all largest 12 ID joltages is {total}")
