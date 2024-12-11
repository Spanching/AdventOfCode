import datetime
import importlib
import sys
import util
import util.input
import time

sample = True

if __name__ == '__main__':
    if len(sys.argv) > 1:
        sample = not sys.argv[1] == "main"

    def _measure_time(foo):
        start = time.time()
        print(foo())
        print(f'took {time.time() - start:.2f}s')

    date = datetime.datetime.now()
    year = date.year
    day = date.day
    input_path = f"{year}/{day:02d}/{'sample_' if sample else ''}input.txt"
    module_path = f"{year}.{day:02d}.tasks"
    daily_module = importlib.import_module(module_path)

    input_method = ""
    if hasattr(daily_module, "input"):
        input_method = daily_module.input()
    match input_method:
        case "raw":
            input = util.input.get_input_as_raw_string(input_path)
        case "oneline":
            input = util.input.get_input_as_one_line_string(input_path)
        case "intlist":
            input = util.input.get_input_as_int_list(input_path)
        case "int":
            input = util.input.get_input_as_oneline_int_list(input_path)
        case _:
            input = util.input.get_input_as_line_list(input_path)

    if hasattr(daily_module, "task1"):
        print(f"DAY {day:02d}: TASK 1")
        _measure_time(lambda: daily_module.task1(input))
    if hasattr(daily_module, "task2"):
        print(f"DAY {day:02d}: TASK 2")
        _measure_time(lambda: daily_module.task2(input))

