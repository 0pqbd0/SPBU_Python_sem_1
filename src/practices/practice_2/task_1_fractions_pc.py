def print_fractions(n):
    for i in range(2, n + 1):
        print(f"1/{i}")
        for j in range(2, i + 1):
            if i % j != 0:
                print(f"{j}/{i}")


if __name__ == "__main__":
    n = int(input("Введите знаменатель: "))
    print_fractions(n)
