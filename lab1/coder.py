a = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ" \
    "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя" \
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
    "abcdefghijklmnopqrstuvwxyz" \
    "1234567890"


while True:
    g = ""
    b = input("Введіть текст: ")
    for i in b:
        now = a.find(i)
        step = 1
        if 0 <= now <= 32:
            now += step
            if now > 32:
                now = now - 33

        if 33 <= now <= 65:
            now += step
            if now > 65:
                now = now - 33

        if 66 <= now <= 91:
            now += step
            if now > 91:
                now = now - 26

        if 92 <= now <= 117:
            now += step
            if now > 117:
                now = now - 26

        if 118 <= now <= 127:
            now += step
            if now > 127:
                now = now - 10

        then = now
        if i in a:
            g += a[then]
        else:
            g += i

    print(g)
