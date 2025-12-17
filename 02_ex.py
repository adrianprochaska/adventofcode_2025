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


def check_duplicate(number):
    number_str = str(number)
    l_half = int(len(number_str) / 2)
    return number_str[:l_half] == number_str[-l_half:]


def check_ntimes(number, rep_hypothesis):
    number_str = str(number)

    if len(number_str) % rep_hypothesis != 0:
        return False

    len_segment = len(number_str) // rep_hypothesis
    for i in range(2, rep_hypothesis + 1):
        if (
            number_str[(i - 1) * len_segment : i * len_segment]
            != number_str[:len_segment]
        ):
            return False
    return True


def check_multiplicities(number):
    number_str = str(number)
    rep_current = number_str.count(number_str[0])
    while rep_current > 1:
        if check_ntimes(number, rep_current):
            return True
        rep_current -= 1
    return False


def check_interval(start, end):
    if len(start) == len(end) and len(start) % 2 == 1:
        return 0
    elif len(start) != len(end):
        # check fist intermediate interval
        sum_1 = check_interval(start, "9" * len(start))
        # check second intermediate interval
        sum_2 = check_interval("1" + len(start) * "0", end)
        return sum_1 + sum_2
    else:
        total = 0
        for number in range(int(start), int(end) + 1):
            if check_duplicate(number):
                total += number
        return total


def check_interval_for_arbitrary_repetitions(start, end):
    total = 0
    for number in range(int(start), int(end) + 1):
        if check_multiplicities(number):
            total += number
    return total


def run(part: int, test: bool):
    # part 1: sum of lines
    if part == 1:
        total = 0
        with open(input_filename(test)) as f:
            line = f.read()
            intervals = line.split(",")
        start_end_matrix = [interval.split("-") for interval in intervals]
        for start_end in start_end_matrix:
            total += check_interval(start_end[0], start_end[1])

            # total += int(line.strip())
        print(f"Part 1: The sum of all fake IDs is {total}")

    # part 2: product of lines
    elif part == 2:
        total = 0
        with open(input_filename(test)) as f:
            line = f.read()
            intervals = line.split(",")
        start_end_matrix = [interval.split("-") for interval in intervals]
        for start_end in start_end_matrix:
            total += check_interval_for_arbitrary_repetitions(
                start_end[0], start_end[1]
            )

            # total += int(line.strip())
        print(f"Part 2: The sum of all fake IDs is {total}")
