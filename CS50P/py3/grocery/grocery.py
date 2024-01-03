list = {}


while True:
    try:
        x = input().upper()
    except EOFError:
        break
    else:
        if x not in list:
            list[x] = 1
        else:
            try:
                list[x] += 1
            except KeyError:
                pass

for item in sorted(list):
    print(list[item], item)