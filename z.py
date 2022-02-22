import string


# number 1
def to_alphabet_pos(t: str) -> list:
    t = t.lower()
    _l = [x for x, i in enumerate(string.ascii_lowercase, 1) if t.find(i) >= 0]
    return _l

    # text = "@%sd$6,psd"
    # to_alphabet_pos(text)


# number 2
def solution(_l: list) -> int:
    number = sum(_l)
    return number // 2

    # solution([8, 2, 8])


# number 3
def wave(t: str) -> list:
    _t = [i for i in t.lower()]
    n = [''.join(_t[:x]) + i.upper() + ''.join(_t[x + 1::]) for x, i in enumerate(t)]
    return n

    # t = 'Hello'
    # wave(t)


# number 4
def encode(_s: str) -> str:
    n = ''
    for x in _s:
        if x == ' ':
            n += x
        elif _s.count(x) >= 2:
            n += ')'
        else:
            n += '('
    return n

    # s = 'hello world'
    # encode(s)


# number 5
def queue_time(l: list, kassa: int) -> int:
    counter = 0
    if kassa == 1:
        return sum(l)
    if len(l) == kassa:
        return max(l)
    while True:
        _ = l[:kassa]
        min_ = min(_)
        _ = [x - min_ for x in _ if x - min_ > 0]
        l[:kassa] = _
        counter += min_
        if len(l) == 1:
            counter += l[0]
            break
    return counter

    # s = queue_time([5, 3, 4], 1)
    # print(s)


# number 6
roman_numerals = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000, '': 0
}


# Римские числа
def get_digit(_str: str) -> int:
    _str = _str.upper()[::-1]
    counter = 0
    n = ''
    for i in _str:
        if roman_numerals[n] > roman_numerals[i]:
            counter -= roman_numerals[i]
            n = i
        elif roman_numerals[n] <= roman_numerals[i]:
            counter += roman_numerals[i]
            n = i
    return counter

    # d = get_digit('xixcm')
    # print(d)


# number 7
def move_zeros(_l: list) -> list:
    counter = [0 for _ in range(_l.count(0))]
    _ = [_l.remove(0) for i in counter]
    _l.extend(counter)
    return _l

    # move_zeros([0, 1, 0, 3, 12])


# number 8
def two_sum(_l: list, num: int) -> list:
    for c2, i in enumerate(_l):
        for c, x in enumerate(_l):
            if i + x == num and c2 != c:
                return [c2, c]
    return list()

    # two_sum([2, 7, 11, 15], 9)


# number 9
def create_phone_number(_l: list) -> str:
    if len(_l) > 10:
        return ''
    number = ''.join(list(map(str, _l)))
    number = f'({number[:3]}) {number[3:6]}-{number[6:]}'
    return number

    # create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])


# number 10
def open_or_senior(data: list) -> list:
    result = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            result.append('Senior')
        else:
            result.append('Open')
    return result

    # open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]])


# number 11
# Нахождение в слове
def in_array(array1: list, array2: list) -> list:
    result = []
    for x in array1:
        for i in array2:
            if x in i and x not in result:
                result.append(x)
    result.sort()
    return result

    # in_array(["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"])


# number 12
# Разделение чисел
def expanded_form(num: int) -> str:
    n = len(str(num))
    result = ''
    for i in range(n + 1):
        zero = ''.join(['0' for x in range(n - i)])
        _ = int('1' + zero)
        s = num // _
        s = s * _
        num -= s
        result += f' + {s}' if s != 0 else ''
    result = result[3:]
    return result

    # expanded_form(72304)


# number 13
# Часы
def make_readable(seconds: int) -> str:
    # Do something
    h = seconds // 3600
    m = (seconds - h * 3600) // 60
    s = (seconds - h * 3600) - m * 60
    result = [f'0{i}' if len(str(i)) <= 1 else f'{i}' for i in (h, m, s)]
    result = ':'.join(result)
    return result

    # make_readable(863)


# number 14
# CamelCase
def to_weird_case(t: str) -> str:
    counter = 0
    n = ''
    for i in t:
        if i != ' ':
            if counter % 2 == 0:
                n += i.upper()
            elif counter % 2 != 0:
                n += i.lower()
            counter += 1
        elif i == ' ':
            counter = 0
            n += i
    return n

    # to_weird_case('This is a test')


# number 15
# Дубликаты
def duplicate_count(text: str) -> int:
    # Your code goes here
    text = text.lower()
    _t = [text.count(i) for i in set(text) if text.count(i) >= 2]
    return len(_t)

    # duplicate_count('Indivisibilities')


# number 16
# Фибоначи
def productFib(prod: int) -> list:
    # your code
    l = [0, 1]
    result = []
    for i in l:
        n1, n2 = l[-2:]
        if (n1 * n2) == prod:
            result.extend([n1, n2])
            result.append(True)
            break
        elif (n1 * n2) > prod:
            result.extend([n1, n2])
            result.append(False)
            break
        l.append(n1 + n2)
    return result

    # productFib(4895)


# number 17
def tower_builder(n_floors: int) -> list:
    # build here
    _l = []
    for i in range(1, n_floors + 1):
        n = ' ' * (n_floors - i) + '*' * i + '*' * (i - 1) + (n_floors - i) * ' '
        _l.append(n)
    return _l

    # tower_builder(3)


# number 18
candidates = [
    {"name": "Petya", "scores": {"math": 92, "russian_language": 33, "computer_science": 34}, "extra_scores": 1},
    {"name": "Vasya", "scores": {"math": 58, "russian_language": 62, "computer_science": 48}, "extra_scores": 0},
    {"name": "Fedya", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
    {"name": "Fedfa", "scores": {"math": 33, "russian_language": 85, "computer_science": 42}, "extra_scores": 2},
]


# number 19
def find_top_20(_candidates: list) -> list:
    _candidates = {i['name']: sum(i['scores'].values(), i['extra_scores']) for i in _candidates}
    result = set()
    ascending = sorted(_candidates.values())[::-1][:20]
    for x in ascending:
        for j in _candidates.keys():
            if _candidates[j] == x:
                result.add(j)
    return list(result)

    # find_top_20(candidates)


# number 20
names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris", "Margo"]
birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001]
genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]


def get_inductees(_names, _birthday_years, _genders) -> list:
    result = []
    for n, b, g in zip(_names, _birthday_years, _genders):
        year = 2021 - (b if b != None else 0)
        if (year >= 18) and (year < 30) and g == 'Male':
            result.append(n)
    return result

    # get_inductees(names, birthday_years, genders)


know_english = ["Vasya", "Jimmy", "Max", "Peter", "Eric", "Zoi", "Felix"]
sportsmen = ["Don", "Peter", "Eric", "Jimmy", "Mark"]
more_than_20_years = ["Peter", "Julie", "Jimmy", "Mark", "Max"]


# number 21
def find_athlets(_know_english: list, _sportsmen: list, _more_than_20_years: list) -> list:
    _know_english = set(_know_english)
    _sportsmen = set(_sportsmen)
    _more_than_20_years = set(_more_than_20_years)
    result = list(_know_english & _sportsmen & _more_than_20_years)
    return result

    # find_athlets(know_english, sportsmen, more_than_20_years)


students_avg_scores = {'Max': 4.964, 'Eric': 4.962, 'Peter': 4.923, 'Mark': 4.957, 'Julie': 4.95,
                       'Jimmy': 4.973, 'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936, 'Zoi': 4.937}

import xlsxwriter


# number 22
def make_report_about_top3(_students_avg_scores):
    workbook = xlsxwriter.Workbook('top_3_students.xlsx')
    worksheet = workbook.add_worksheet()
    result = []
    for i in sorted(_students_avg_scores.values())[::-1][:3]:
        for x in _students_avg_scores.keys():
            if _students_avg_scores[x] == i:
                result.append(x)
    _ = [worksheet.write(f'A{c}', j) for c, j in enumerate(result, 1)]
    workbook.close()
    return result

    # make_report_about_top3(students_avg_scores)
