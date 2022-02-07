import itertools
import matplotlib.pyplot as plt

POINT_POST = (0, 2)
WITHOUT_POST = (2, 5), (5, 2), (6, 6), (8, 3)


def get_route_length(points):
    route_length_list = []
    route_length = 0.0
    current = points[0]
    for next_point in points[1:]:
        route_length += (
            (next_point[0] - current[0]) ** 2 + (next_point[1] - current[1]) ** 2
        ) ** 0.5
        route_length_list.append(route_length)
        current = next_point
    return route_length_list


min_way = float("inf")
route_min = None
way = 0.0
for route_without_post in itertools.permutations(WITHOUT_POST):
    route_all = (POINT_POST,) + route_without_post + (POINT_POST,)
    way = get_route_length(route_all)[-1]
    if way < min_way:
        min_way = way
        route_min = route_all

list_result = list(zip(route_min[1:], get_route_length(route_min)))
str_result = [str(POINT_POST)]
for point, length in list_result:
    str_result.append(f"{point}[{length}]")
print_route = (" -> ".join(str_result)) + " = " + str(min_way)


def draw_route(route):
    plt.figure()
    x, y = zip(*route)
    plt.plot(x, y, color="red", ls="-", alpha=1)
    for i, i_x, i_y in zip(range(len(route) - 1), x, y):
        plt.text(i_x, i_y, f"{i + 1} ({i_x}, {i_y})")
    plt.grid()
    plt.show()
