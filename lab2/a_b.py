a = input("Виберіть дію: a/b")


if a == "a":
    t = input("Введіть текст:")
    x = t.split()
    b = sorted(x)
    z = 1
    y = len(b)

    print(b[0])
    while z < y:
        if b[z] == b[z-1]:
            z += 1
            continue

        print(b[z])
        z += 1

if a == "b":
    t = str.lower(input("Введіть текст:"))

    d = {}
    for i in set(t):
        d[i] = t.count(i)
    print(d)