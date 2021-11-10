b = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ" \
    "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя" \
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
    "abcdefghijklmnopqrstuvwxyz" \
    "1234567890"



def decoder(text, step):
    result = ""

    for i in text:
        now = b.find(i)

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
        if i in b:
            result += b[then]
        else:
            result += i

    return result