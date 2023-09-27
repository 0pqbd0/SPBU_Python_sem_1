def find_quotient(a, b):
    quotient = 0
    remains = abs(a)
    while remains >= abs(b):
        remains -= abs(b)
        quotient += 1
    if (a > 0 > b) or (a < 0 < b):
        return -quotient
    else:
        return quotient


if __name__ == '__main__':
    divisible = int(input("Введите делимое:"))
    divider = int(input("Введите делитель:"))
    print("Неполное частное:", find_quotient(divisible, divider), sep="")