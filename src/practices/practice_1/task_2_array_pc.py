def reorder(array, len_1):
    array[len_1:], array[:len_1] = array[:len_1], array[len_1:]
    return array


if __name__ == "__main__":
    length_1 = int(input("Введите количество элементов в первой части:"))
    array = [int(num) for num in input("Введите вектор: ").split()]
    print(reorder(array, length_1))
