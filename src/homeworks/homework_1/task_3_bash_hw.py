import sys
import os


def find_file(file_name):
    current_path = os.path.abspath(__file__)
    part_path, _ = os.path.split(current_path)
    file_path = os.path.join(part_path, file_name)
    return file_path


def wc(arguments, path):
    with open(path) as f:
        if not arguments:
            return str(sum(1 for line in f)) + str(sum(len(line.split()) for line in f)) + str(os.path.getsize(path))

        elif arguments[0] == "-c" or arguments[0] == "--bytes":
            return str(os.path.getsize(path))

        elif arguments[0] == "-m" or arguments[0] == "--count":
            return str(sum(len(line) for line in f))

        elif arguments[0] == "-l" or arguments[0] == "--lines":
            return str(sum(1 for line in f))

        elif arguments[0] == "-w" or arguments[0] == "--words":
            return str(sum(len(line.split()) for line in f))


def take_lines(command, count, path):
    with open(path) as f:
        if command == "head":
            lines = ''.join([next(f) for i in range(count)])
        elif command == "tail":
            lines = ''.join(f.readlines()[-count:])
    return lines


def head(arguments, path):
    if not arguments:
        return take_lines("head", 10, path)
    elif arguments[0] == "-c" or arguments[0] == "--bytes":
        c = int(arguments[1])
        with open(path, 'r', encoding='utf-8') as f:
            data = f.read(c)
        return data
    elif arguments[0] == "-n" or arguments[0] == "--lines":
        return take_lines("head", int(arguments[1]), path)


def tail(arguments, path):
    if not arguments:
        return take_lines("tail", 10, path)
    elif arguments[0] == "-c" or arguments[0] == "--bytes":
        c = int(arguments[1])
        with open(path, 'r', encoding='utf-8') as f:
            lines = ''.join(f.read()[-c:])
        return lines
    elif arguments[0] == "-n" or arguments[0] == "--lines":
        return take_lines("tail", int(arguments[1]), path)

def print_commands(command, arguments, out, file_name):
    print(f'{command} {" ".join(map(str, arguments))} {file_name} :  {out}')


if __name__ == '__main__':
    file_path = find_file(sys.argv[-1])
    command = sys.argv[1]
    arguments = sys.argv[2: -1]
    if command == "wc":
        print_commands(command, arguments, wc(arguments, file_path), sys.argv[-1])
    elif command == "head":
        print_commands(command, arguments, head(arguments, file_path), sys.argv[-1])
    elif command == "tail":
        print_commands(command, arguments, tail(arguments, file_path), sys.argv[-1])