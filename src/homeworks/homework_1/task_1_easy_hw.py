def calculate_polynom(x):
    x_square = x * x
    return (x_square + 1) * (x_square + x) + 1


if __name__ == '__main__':
    x = int(input("Calculating x^4+x^3+x^2+x+1, enter x:"))
    print(f'{x}^4+{x}^3+{x}^2+{x}+1=', calculate_polynom(x), sep="")