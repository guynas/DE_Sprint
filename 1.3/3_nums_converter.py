#!/usr/bin/env python3

print("Enter an Arabic number in range 1..2000 to convert to Roman:")
num = int(input())

ls = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
dict = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
}


def func(num):
    ls2 = []
    res = ""

    def func2(num, res):
        for i in range(0, len(ls)):
            if num in ls:
                res = dict[num]
                rem = 0
                break
            if ls[i] < num:
                quo = num // ls[i]
                rem = num % ls[i]
                res = res + dict[ls[i]] * quo
                break
        ls2.append(res)
        if rem == 0:
            pass
        else:
            func2(rem, "")

    func2(num, res)
    return "".join(ls2)


print(func(num))
