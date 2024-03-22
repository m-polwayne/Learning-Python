def operation(num1, num2, num3, num):
    print(locals())

    def low(a, b, c, d):
        print(locals())
    low(1, 2, 3, 4)


operation(1, 2, 3, 4,)

print(locals())


def another(num1, num4, num2, num3, num):
    j = locals()
    print(j)
    j.update({"num6": 6})
    j["num7"] = 7
    print(j)


another(1, 4, 2, 3, 5)
