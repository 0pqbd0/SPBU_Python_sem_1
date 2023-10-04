def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_prime(n):
    for i in range(2, n + 1):
        if is_prime(i):
            print(i)


if __name__ == "__main__":
    n = int(input("Введите число:"))
    find_prime(n)
