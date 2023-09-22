import sys
import os
import csv

def find_file(file_name):
    current_path = os.path.abspath(__file__)
    part_path, _ = os.path.split(current_path)
    file_path = os.path.join(part_path, file_name)
    return file_path


def writing_to_a_file(path, freqs):
    with open(path, 'w') as file_to_write:
        writer = csv.writer(file_to_write)
        for key in freqs:
            writer.writerow([key, freqs[key]])


def count_freqs(path):
    freqs = {}
    with open(path, "r") as f_from:
        for line in f_from:
            for word in line.split( ):
                freqs[word] = freqs.get(word, 0) + 1
    return freqs


if __name__ == "__main__":
    file_path = find_file(sys.argv[1])
    file_to_write_path = find_file(sys.argv[2])
    writing_to_a_file(file_to_write_path, count_freqs(file_path))


