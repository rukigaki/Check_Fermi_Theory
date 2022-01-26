class MyException(Exception):
    pass


def check_fermi_theory():
    number = []
    print('Введите натуральные числа a, b, c и n, которые больше двух')

    def input_number_not_word_or_symbol():

        try:
            n = int(input("Введите число, а не букв(у/ы) " + s + ": "))
            if n < 3:
                raise MyException
        except ValueError:
            n = input_number_not_word_or_symbol()
        except MyException:
            n = input_number_more_than_two()
        return n

    def input_number_more_than_two():
        try:
            n = int(input('Введите натуральное число ' + s + ' больше двух: '))
            if n < 3:
                raise MyException
        except ValueError:
            n = input_number_not_word_or_symbol()
        except MyException:
            n = input_number_more_than_two()
        return n

    for i in ["a", "b", "c", "n"]:

        try:
            s = i
            n2 = int(input("Введите " + i + ": "))
            if n2 < 3:
                raise MyException
            number.append(n2)

        except ValueError:
            number.append(int(input_number_not_word_or_symbol()))
        except MyException:
            number.append(int(input_number_more_than_two()))
    number_n = number[3]
    a = number[0] ** number_n
    b = number[1] ** number_n
    c = number[2] ** number_n
    if a + b == c:
        print('a^n + b^n = c^n',
              str(a + b) + " = " + str(c),
              "Ферма. братан, ты ошибся", sep="\n")
    else:
        print('a^n + b^n != c^n',
              str(a + b) + " != " + str(c),
              'Ферма, братан, твоя теория работает как швецарские часы', sep="\n")


check_fermi_theory()
