import math


def read_circle_data(file_path):
    with open(file_path, 'r') as f:
        x_center, y_center = map(float, f.readline().split())
        radius = float(f.readline())
    return x_center, y_center, radius


def read_points(file_path):
    points = []
    with open(file_path, 'r') as f:
        for line in f:
            x, y = map(float, line.split())
            points.append((x, y))
    return points


def point_position(x_center, y_center, radius, x, y):
    distance_squared = (x - x_center)**2 + (y - y_center)**2
    radius_squared = radius ** 2
    if distance_squared < radius_squared:
        return 1
    elif distance_squared == radius_squared:
        return 0
    else:
        return 2


def main():
    circle_file = input("Введите путь к файлу с данными об окружности: ")
    points_file = input("Введите путь к файлу с данными о точках: ")

    x_center, y_center, radius = read_circle_data(circle_file)
    points = read_points(points_file)

    for (x, y) in points:
        print(point_position(x_center, y_center, radius, x, y))


if __name__ == '__main__':
    main()