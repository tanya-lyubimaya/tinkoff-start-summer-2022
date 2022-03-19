ab, ac, bc = input(), input(), input()

if ab == ">":
    if ac == ">":
        if bc == ">":
            print("cba")
        elif bc == "<":
            print("bca")
        elif bc == "=":
            print("bca")
            print("cba")
    elif ac == "<" and bc == "<":
        print("bac")
    elif ac == "=" and bc == "<":
        print("bac")
        print("bca")
elif ab == "<":
    if ac == ">" and bc == ">":
        print("cab")
    elif ac == "<":
        if bc == ">":
            print("acb")
        elif bc == "<":
            print("abc")
        elif bc == "=":
            print("abc")
            print("acb")
    elif ac == "=" and bc == ">":
        print("acb")
        print("cab")
elif ab == "=":
    if ac == ">" and bc == ">":
        print("cab")
        print("cba")
    elif ac == "<" and bc == "<":
        print("abc")
        print("bac")
    elif ac == "=" and bc == "=":
        print("abc")
        print("acb")
        print("bac")
        print("bca")
        print("cab")
        print("cba")
