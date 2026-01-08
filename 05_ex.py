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


def load_input(test):
    with open(input_filename(test)) as f:
        file = f.read()
    intervals, ids = file.split("\n\n")
    intervals = [list(map(int, row.split("-"))) for row in intervals.splitlines()]
    intervals.sort()
    intervals = [[interval[0] for interval in intervals]] + [
        [interval[1] for interval in intervals]
    ]
    ids = list(map(int, ids.splitlines()))
    ids.sort()

    return intervals, ids


def condense_intervals(sorted_intervals):
    starts = sorted_intervals[0]
    ends = sorted_intervals[1]
    starts_condensed = [starts[0]]
    ends_condensed = [ends[0]]
    for idx in range(1, len(starts)):
        if starts[idx] <= ends_condensed[-1] and ends[idx] >= ends_condensed[-1]:
            ends_condensed[-1] = ends[idx]
        else:
            starts_condensed.append(starts[idx])
            ends_condensed.append(ends[idx])

    return [starts_condensed] + [ends_condensed]


def calc_freshness(id, intervals):
    starts = intervals[0]
    ends = intervals[1]

    # cornercases bigger than biggest or smaller than smallest
    if id < starts[0] or id > ends[-1]:
        return False

    for idx in range(len(starts)):
        if id >= starts[idx] and id <= ends[idx]:
            return True
        if id < starts[idx]:
            return False

    return False


def run(part: int, test: bool):
    # part 1: sum of lines
    if part == 1:
        total = 0
        intervals, ids = load_input(test)
        intervals_condensed = condense_intervals(intervals)

        for id in ids:
            freshness = calc_freshness(id, intervals_condensed)
            if freshness:
                total += 1

        print(f"Part 1: The sum of all fresh IDs is {total}")

    # part 2: product of lines
    elif part == 2:
        total = 0
        intervals, ids = load_input(test)
        intervals_condensed = condense_intervals(intervals)

        total = sum(
            list(
                map(
                    lambda x, y: y - x + 1,
                    intervals_condensed[0],
                    intervals_condensed[1],
                )
            )
        )
        print(f"Part 2: The product of all ingredient IDs is {total}")
