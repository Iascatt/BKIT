import sys
import math


def input_float(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        string: Введенная строка
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        try:
            print(prompt)
            coef_str = input()
        except KeyboardInterrupt:
            print("Ввод прерван. Выход из программы.")
            sys.exit()
    return coef_str


def get_coef(index, prompt):
    '''
    Преобразовываем коээфициент из string в float
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    # Переводим строку в действительное число
    got_float = False
    coef = None
    while not got_float:
        try:
            coef = float(input_float(index, prompt))
        except ValueError:
            print("Значение некорректно, попробуйте еще раз")
        else:
            got_float = True
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        bool: ограничено ли множество корней
        list[float]: Список корней
    '''
    result2 = []
    result = []
    D = b * b - 4 * a * c
    if a == 0:
        # bx + c = 0
        if b == 0:
            # c == 0, x - любое
            if c == 0:
                return False, result
            # c != 0, нет корней
            return True, result
        # b != 0, c != 0, 1 корень
        result2.append(-c / b)
    elif D == 0.0:
        root = -b / (2.0 * a)
        result2.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)
        result2.append(root1)
        result2.append(root2)
    for i in result2:
        if i > 0:
            result.append(math.sqrt(i))
            result.append(-math.sqrt(i))
        elif i == 0:
            result.append(math.sqrt(i))
    return True, result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    is_limited, roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if not is_limited:
        print("Бесконечно много корней")
    elif len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {:.3f}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {:.3f} и {:.3f}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {:.3f}, {:.3f} и {:.3f}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {:.3f}, {:.3f}, {:.3f} и {:.3f}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4