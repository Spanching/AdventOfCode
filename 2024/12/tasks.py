from collections import deque

DIRECTIONS = [1, -1, 1j, -1j]

def group_plots(garden):
    plants, visited = [], set()
    for plot in garden:
        if plot in visited:
            continue
        group = bfs(garden, plot)
        plants.append(group)
        visited |= group
    return plants


def bfs(garden: dict[complex, chr], plot):
    queue, visited = deque([plot]), set()
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        for direction in DIRECTIONS:
            new_plot = current + direction
            if garden.get(new_plot) == garden.get(current):
                queue.append(new_plot)
    return visited


def get_perimeter(garden, group):
    perimeter = set()
    for plot in group:
        for direction in DIRECTIONS:
            new_plot = plot + direction
            if new_plot not in garden or garden[new_plot] != garden[plot]:
                perimeter.add((new_plot, plot))
    return perimeter


def task1(puzzle_input):
    garden = {
        complex(i, j): char
        for i, line in enumerate(puzzle_input)
        for j, char in enumerate(line)
    }
    groups = group_plots(garden)
    return sum(len(group) * len(get_perimeter(garden, group)) for group in groups)


def get_side(perimeter, border):
    side_queue = deque([border])
    visited = set()
    directions = [-1j, 1j] if border[0].imag == border[1].imag else [-1, 1]
    while side_queue:
        current = side_queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        outside, inside = current
        for direction in directions:
            new_border = (outside + direction, inside + direction)
            if new_border in perimeter:
               side_queue.append(new_border)
    return visited


def calculate_number_of_sides(garden, group):
    perimeter = get_perimeter(garden, group)
    count = 0
    while perimeter:
        border = next(iter(perimeter))
        perimeter -= get_side(perimeter, border)
        count += 1
    return count


def task2(puzzle_input):
    garden = {
        complex(i, j): char
        for i, line in enumerate(puzzle_input)
        for j, char in enumerate(line)
    }
    groups = group_plots(garden)
    return sum(len(group) * calculate_number_of_sides(garden, group) for group in groups)
