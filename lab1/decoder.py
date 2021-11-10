a = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя" \
    "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ" \
    "abcdefghijklmnopqrstuvwxyz" \
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
    "1234567890"


while True:
    b = input("Введіть текст:")
    result = ""
    for i in b:
        now = a.find(i)
        step = 1
        if 0 <= now <= 32:
            now -= step
            if now < 0:
                now = now + 33
        if 33 <= now <= 65:
            now -= step
            if now < 33:
                now = now + 33
        if 66 <= now <= 91:
            now -= step
            if now < 66:
                now = now + 26
        if 92 <= now <= 117:
            now -= step
            if now < 92:
                now = now + 26
        if 118 <= now <= 127:
            now -= step
            if now < 118:
                now = now + 10

        then = now
        if i in a:
            result += a[then]
        else:
            result += i

    print(result)