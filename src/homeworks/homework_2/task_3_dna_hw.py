import sys
import os


def find_file(file_name):
    current_path = os.path.abspath(__file__)
    part_path, _ = os.path.split(current_path)
    file_path = os.path.join(part_path, file_name)
    return file_path


def writing_to_a_file(path, dna):
    if os.path.isfile(path):
        with open(path, 'w') as file_to_write:
            for letter in dna:
                file_to_write.write(letter)
    else:
        print("Такого файла не существует")


def delete_dna(start, end, current_dna):
    part_of_dna = current_dna[current_dna.index(start) + len(start):]
    return current_dna[:current_dna.index(start)] + part_of_dna[part_of_dna.index(end) + len(end):]


def insert_dna(start, fragment, current_dna):
    return current_dna[:current_dna.index(start) + len(start)] + fragment + current_dna[current_dna.index(start) + len(start):]


def replace_dna(template, fragment, current_dna):
    return current_dna.replace(template, fragment, 1)


def read_command(path):
    with open(path, 'r') as log_file:
        log_file.readline()
        dna = log_file.readline()
        log_file.readline()
        for line in log_file:
            command, first_parametr, second_parametr = line.split( )
            if command == 'DELETE':
                dna = delete_dna(first_parametr, second_parametr, dna)
            if command == 'INSERT':
                dna = insert_dna(first_parametr, second_parametr, dna)
            if command == 'REPLACE':
                dna = replace_dna(first_parametr, second_parametr, dna)
    return dna


if __name__ == "__main__":
    file_path = find_file(sys.argv[1])
    file_to_write_path = find_file(sys.argv[2])
    writing_to_a_file(file_to_write_path, read_command(file_path))
