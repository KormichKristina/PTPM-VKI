import logging
import sys
import math

log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    level=logging.DEBUG,
    format=log_format,
    datefmt=date_format,
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

def calculate_triangle(a, b, c):
    logging.info("Начало вычисления треугольника")

    if a <= 0 or b <= 0 or c <= 0:
        logging.error("Стороны должны быть положительными")
        return "не треугольник", [(-1, -1)] * 3

    if a + b <= c or a + c <= b or b + c <= a:
        logging.warning("Треугольник с такими сторонами не существует")
        return "не треугольник", [(-1, -1)] * 3

    if a == b == c:
        triangle_type = "равносторонний"
    elif a == b or a == c or b == c:
        triangle_type = "равнобедренный"
    else:
        triangle_type = "разносторонний"

    # Координаты первой и второй вершин
    x1, y1 = 0, 0
    x2, y2 = int(a), 0

    # Вычисление координат третьей вершины
    x3 = (b * b + a * a - c * c) / (2 * a)
    y3 = math.sqrt(max(0, b * b - x3 * x3))

    coordinates = [
        (x1, y1),
        (x2, y2),
        (int(round(x3)), int(round(y3)))
    ]

    # Проверка попадания координат в поле 100x100
    if any(x < 0 or x >= 100 or y < 0 or y >= 100
           for x, y in coordinates):
        logging.warning("Вершины выходят за пределы поля 100x100")

    logging.info("Тип треугольника: %s", triangle_type)
    logging.info("Координаты вершин: %s", coordinates)

    return triangle_type, coordinates


def main():
    logging.info("Приложение запущено")

    try:
        a = float(input("Введите сторону A: "))
        b = float(input("Введите сторону B: "))
        c = float(input("Введите сторону C: "))

        triangle_type, coordinates = calculate_triangle(a, b, c)

        print("Тип треугольника:", triangle_type)
        print("Координаты вершин:", coordinates)

    except ValueError:
        logging.error("Введены некорректные данные")
        print("Ошибка: необходимо вводить числа")

    except Exception:
        logging.exception("Произошла непредвиденная ошибка")

    logging.info("Приложение завершено")


if __name__ == "__main__":
    main()