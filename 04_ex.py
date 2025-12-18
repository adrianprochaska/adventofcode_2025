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


def parse_input(input):
    one_str = "@"
    lines = input.split("\n")
    dummy_line = [0] * (len(lines[0]) + 2)
    matrix = [dummy_line]
    for line in lines:
        matrix.append(
            [0] + list(map(int, list(line.replace(".", "0").replace("@", "1")))) + [0]
        )
    matrix.append(dummy_line)

    return matrix


def count_neighbors(rolls_matrix, count_threshold=4, remove=False):
    neighbors = 1

    n_rows = len(rolls_matrix)
    row_indices = range(1, n_rows - 1)

    n_cols = len(rolls_matrix[0])
    col_indices = range(1, n_cols - 1)

    adj_matrix = []
    for idx in range((n_rows)):
        adj_matrix.append((n_cols) * [0])
    count = 0

    for row_idx in row_indices:
        for col_idx in col_indices:
            if rolls_matrix[row_idx][col_idx]:
                adj_loc = sum(
                    [
                        sum(row[col_idx - neighbors : col_idx + neighbors + 1])
                        for row in rolls_matrix[
                            row_idx - neighbors : row_idx + neighbors + 1
                        ]
                    ]
                )
                adj_matrix[row_idx][col_idx] = adj_loc
                if adj_loc <= count_threshold:
                    count += 1
                    rolls_matrix[row_idx][col_idx] = 0

    return rolls_matrix, count


def run(part: int, test: bool):
    # part 1: sum of lines
    if part == 1:

        with open(input_filename(test)) as f:
            input = f.read()
        rolls_matrix = parse_input(input)
        adj_matrix, count = count_neighbors(rolls_matrix, count_threshold=4)

        print(f"Part 1: The sum of all relevant rolls is {count}")

    # part 2: product of lines
    elif part == 2:
        count = 0
        with open(input_filename(test)) as f:
            input = f.read()
        rolls_matrix = parse_input(input)

        # remove rolls
        remove_count = 999
        while remove_count > 0:
            rolls_matrix, remove_count = count_neighbors(
                rolls_matrix, count_threshold=4
            )
            count += remove_count

        print(f"Part 2: The sum of all removed rolls is {count}")
