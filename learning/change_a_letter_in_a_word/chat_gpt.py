import test
def OneEditApart(str1, str2):
    # Получаем длину строк
    len1 = len(str1)
    len2 = len(str2)

    # Если разница в длине больше 1, то строки не могут отличаться только одним действием
    if abs(len1 - len2) > 1:
        return False

    # Инициализируем переменные
    count = 0
    i = 0
    j = 0

    # Проходимся по обеим строкам
    while i < len1 and j < len2:
        # Если символы равны, переходим к следующему символу
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            # Иначе увеличиваем счетчик отличающихся символов
            count += 1
            if count > 1:
                return False
            # Если длины строк разные, то двигаем указатель только у той строки, у которой длина больше
            if len1 > len2:
                i += 1
            elif len2 > len1:
                j += 1
            else:
                # Если длины строк равны, то двигаем указатель у обеих строк
                i += 1
                j += 1

    # Если одна строка закончилась, а другая еще осталась, то считаем это за еще одно отличие
    if i < len1 or j < len2:
        count += 1

    # Если отличий больше 1, то строки не могут отличаться только одним действием
    if count > 1:
        return False

    return True


if __name__ == "__main__":
    test.assert_equals(OneEditApart("cat", "dog"), False)
    test.assert_equals(OneEditApart("cat", "caats"), False)
    test.assert_equals(OneEditApart("cat", "cats"), True)
    test.assert_equals(OneEditApart("cat", "ccat"), True)
    test.assert_equals(OneEditApart("cat", "ccccat"), False)
    test.assert_equals(OneEditApart("cat", "catt"), True)
    test.assert_equals(OneEditApart("cat", "catttt"), False)
    test.assert_equals(OneEditApart("cat", "bcat"), True)
    test.assert_equals(OneEditApart("cat", "at"), True)
    test.assert_equals(OneEditApart("cat", "ca"), True)
    test.assert_equals(OneEditApart("cat", "cut"), True)
    test.assert_equals(OneEditApart("cat", "cast"), True)
    test.assert_equals(OneEditApart("cat", "acts"), False)
    test.assert_equals(OneEditApart("cat", "act"), True)
    test.assert_equals(OneEditApart("cat", "tct"), False)
    test.assert_equals(OneEditApart("sister", "tsiter"), False)
    test.assert_equals(OneEditApart("sister", "sister"), True)
    test.assert_equals(OneEditApart("sister", "ssister"), True)
    test.assert_equals(OneEditApart("sister", "sssister"), False)
    test.assert_equals(OneEditApart("sister", "sisterr"), True)
    test.assert_equals(OneEditApart("sister", "sisterrr"), False)
    test.assert_equals(OneEditApart("sister", "siter"), True)
    test.assert_equals(OneEditApart("sister", "sisrter"), True)