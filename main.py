def proverka(check):
    if check % 2 == 0:
        return check == 2
    delitel = 3
    while delitel * delitel <= check and check % delitel != 0:
        delitel += 2
    return delitel * delitel > check


def delimost(e_delimost, e_check_delimost):
    if e_check_delimost % e_delimost == 0:
        return False
    if e_delimost % 2 == 0 and e_check_delimost % 2 == 0:
        return False
    delitel = 3
    while delitel * delitel <= e_delimost and (e_delimost % delitel != 0 or e_check_delimost % delitel != 0):
        delitel += 2
    return delitel * delitel > e_delimost


alphabet = {' ': 0, 'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5, 'е': 6, 'ё': 7, 'ж': 8, 'з': 9, 'и': 10, 'к': 12,
            'й': 11, 'л': 13, 'м': 14, 'н': 15, 'о': 16, 'п': 17, 'р': 18, 'с': 19, 'т': 20, 'у': 21, 'ф': 22,
            'х': 23, 'ц': 24, 'ч': 25, 'ш': 26, 'щ': 27, 'ъ': 28, 'ы': 29, 'ь': 30, 'э': 31, 'ю': 32, 'я': 33}
reversed_alphabet = [' ', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'к',
                     'й', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
                     'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
print("Введите комманду: зашифровать или расшифровать")
command = input().lower()
if command == "зашифровать":
    print("Узнайте и введите публичные ключи.")
    print("Введите ключ 'e': ")
    e = int(input())
    print("Введите ключ 'n': ")
    n = int(input())
    print("Введите сообщение: ")
    soobshenie = list(input().lower())
    shifr_soobshenie = soobshenie
    i = 0
    while i < len(soobshenie):
        soobshenie[i] = (int(alphabet[soobshenie[i]]) ** e) % n
        while soobshenie[i] > 33:
            soobshenie[i] -= 34
        shifr_soobshenie[i] = reversed_alphabet[soobshenie[i]]
        i += 1
    print(str(shifr_soobshenie))
elif command == "расшифровать":
    print("Введите простое число.")
    p = int(input())
    condition = proverka(p)
    while not condition:
        print("Некорректное число.")
        print("Введите простое число.")
        p = int(input())
        condition = proverka(p)
    print("Введите другое простое число.")
    q = int(input())
    condition = proverka(q)
    while not condition or q == p:
        print("Некорректное число.")
        print("Введите другое простое число.")
        q = int(input())
        condition = proverka(q)
    n = p * q
    e_check = (p - 1) * (q - 1)
    print("Введите число меньше чем %s, больше, чем 1 и не имеющее с ним общих делителей кроме 1." % e_check)
    e = int(input())
    condition = delimost(e, e_check)
    while e_check <= e < 1 or not condition:
        print("Некорректное число.")
        print("Введите число меньше чем %s, не имеющее с ним общих делителей кроме 1." % e_check)
        e = int(input())
        condition = delimost(e, e_check)
    print("Введите закрытый ключ d, остаток от деления на ", e_check, " произведения с ", e, " которого равен 1 : ")
    d = int(input())
    print("d = %s" % d)
    print("Сообщите собеседнику открытый ключ - %s" % e, n)
    print("Введите зашифрованное сообщение: ")
    shifr_soobshenie = list(input().lower())
    soobshenie = shifr_soobshenie
    i = 0
    while i < len(shifr_soobshenie):
        shifr_soobshenie[i] = (int(alphabet[shifr_soobshenie[i]]) ** d) % n
        while shifr_soobshenie[i] > 33:
            shifr_soobshenie[i] -= 34
        soobshenie[i] = reversed_alphabet[shifr_soobshenie[i]]
        i += 1
    print(str(soobshenie))
else:
    print("Некорректная комманда")
