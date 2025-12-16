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


def subtract(a, b, min_lim, max_lim):
    return remove_overflow(a - b, min_lim, max_lim)


def add(a, b, min_lim, max_lim):
    return remove_overflow(a + b, min_lim, max_lim)


def remove_overflow(a, min_lim, max_lim):
    divisor = max_lim - min_lim + 1
    remainder = a % divisor
    quotient = a // divisor
    abs_quotient = abs(quotient)
    if remainder == 0 and quotient < 1:
        abs_quotient += 1

    return remainder, abs_quotient


def run(part: int, test: bool):
    # part 1: sum of lines
    dial_number = 50
    min_number = 0
    max_number = 99
    operations = {"L": subtract, "R": add}
    count_zero = 0

    if part == 1:
        with open(input_filename(test)) as f:
            for line in f:
                dial_number = operations[line[0]](dial_number, int(line.strip()[1:]), min_number, max_number)
                if dial_number == 0:
                    count_zero += 1

        print(f"Part 1: The sum of all counted zeros is {count_zero}")

    # part 2: product of lines
    elif part == 2:
        with open(input_filename(test)) as f:
            for line in f:
                new_number, has_overflow = operations[line[0]](dial_number, int(line.strip()[1:]), min_number, max_number)
                if has_overflow and dial_number == 0 and line[0] == "L":
                    has_overflow -= 1
                count_zero += has_overflow
                dial_number = new_number
        
        print(f"Part 2: The sum of all counted zeros is {count_zero}")
