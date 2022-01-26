class MyException(Exception):
    pass


def check_fermi_theory():
    number = []
    print('Введите натуральные числа a, b, c и n, которые больше двух')

    def input_number_not_word_or_symbol():

        try:
            number_local = int(input("Введите число, а не букв(у/ы) " + s + ": "))
            if number_local < 3:
                raise MyException
        except ValueError:
            number_local = input_number_not_word_or_symbol()
        except MyException:
            number_local = input_number_more_than_two()
        return number_local

    def input_number_more_than_two():
        try:
            number_local = int(input('Введите натуральное число ' + s + ' больше двух: '))
            if number_local < 3:
                raise MyException
        except ValueError:
            number_local = input_number_not_word_or_symbol()
        except MyException:
            number_local = input_number_more_than_two()
        return number_local

    for i in ["a", "b", "c", "n"]:

        try:
            s = i
            number_global = int(input("Введите " + i + ": "))
            if number_global < 3:
                raise MyException
            number.append(number_global)

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
