import sys
import os


def find_file(file_name):
    current_path = os.path.abspath(__file__)
    part_path, _ = os.path.split(current_path)
    file_path = os.path.join(part_path, file_name)
    if not os.path.isfile(file_path):
        print(f"Ошибка! Файл с именем: '{file_name}' не найден.")
        return None
    return file_path


def sort_data(a, b, file_in):
    list1 = []
    list2 = []
    list3 = []
    with open(file_in) as f_in:
        for line in f_in:
            for num in line.split():
                if int(num) < int(a):
                    list1.append(num)
                elif int(a) <= int(num) <= int(b):
                    list2.append(num)
                else:
                    list3.append(num)
    return list1, list2, list3


def write_data(file_out, *lists):
    with open(file_out, 'w') as f_out:
        for lst in lists:
            f_out.write(' '.join(lst) + '\n')


if __name__ == "__main__":
    num_1 = sys.argv[1]
    num_2 = sys.argv[2]
    file_in_path = find_file(sys.argv[-2])
    file_out_path = find_file(sys.argv[-1])
    if not file_in_path:
        if file_out_path:
            print(
                f"Ошибка! Файла с именем: '{sys.argv[-2]}' не существует, "
                f"но файл для вывода с именем '{sys.argv[-1]}' существует")
        sys.exit(1)
    write_data(file_out_path, *sort_data(num_1, num_2, file_in_path))
