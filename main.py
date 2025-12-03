import argparse

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Advent of Code 2025")
    parser.add_argument(
        "--exercise", type=int, help="Exercise number to run", required=True
    )
    parser.add_argument(
        "--part", type=int, help="Part number to run", required=False, default=1
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run test input instead of real input",
        required=False,
        default=False,
    )
    args = parser.parse_args()
    exercise_number = args.exercise
    part_number = args.part
    use_test_input = args.test
    # Dynamically import and run the specified exercise
    exercise_module_name = f"{exercise_number:02d}_ex"
    exercise_module = __import__(exercise_module_name)
    exercise_module.run(part_number, use_test_input)
