import datetime
import importlib
import sys
import util
import util.input
import time

sample = False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        sample = sys.argv[1] == "sample"

    def _measure_time(foo):
        start = time.time()
        print(foo())
        print(f'took {time.time() - start:.2f}s')

    date = datetime.datetime.now()
    year = date.year
    day = 6 #date.day
    input_path = f"{year}/{day:02d}/{'sample_' if sample else ''}input"
    module_path = f"{year}.{day:02d}.{day:02d}"

    daily_module = importlib.import_module(module_path)

    input = util.input.get_input_as_line_list(input_path)

    if hasattr(daily_module, "task1"):
        print(f"DAY {day:02d}: TASK 1")
        _measure_time(lambda: daily_module.task1(input))
    if hasattr(daily_module, "task2"):
        print(f"DAY {day:02d}: TASK 2")
        _measure_time(lambda: daily_module.task2(input))

