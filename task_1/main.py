from task_1.app import postman as p


def main():
    print('Результат работы программы:')
    print(p.print_route)
    p.draw_route(p.route_min)


if __name__ == '__main__':
    main()
