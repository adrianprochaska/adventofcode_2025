# template for each days exercise file

def get_day() -> int:
    # find day number from filename
    import os
    filename = os.path.basename(__file__)
    day_str = filename.split('_')[0]
    return int(day_str)

def input_filename(test: bool) -> str:
    day = get_day()
    if test:
        return f"{day:02d}_test.txt"
    else:
        return f"{day:02d}_in.txt"

def run(part: int, test: bool):
    # part 1: sum of lines
    if part == 1:
        total = 0
        with open(input_filename(test)) as f:
            for line in f:
                total += int(line.strip())
        print(f"Part 1: The sum of all lines is {total}")


    # part 2: product of lines
    elif part == 2:
        product = 1
        with open(input_filename(test)) as f:
            for line in f:
                product *= int(line.strip())
        print(f"Part 2: The product of all lines is {product}")

