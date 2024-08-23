import os
import collections
import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Analyze logs')
    parser.add_argument('path', help='Path to logs files')
    parser.add_argument("--text", help="Text to search in logs")
    parser.add_argument(
        "--full", help="Show all occurrences of the text in logs, or only the first one", action="store_true"
    )
    args = parser.parse_args()

    return args.path, args.text, args.full


def get_files_with_extension(directory, extension):
    files_with_extension = [filename for filename in os.listdir(directory) if filename.endswith(extension)]
    return files_with_extension


def read_file(g_path):
    with open(g_path, 'r') as file:
        for line in file.readlines():
            yield line


def search_text_in_line(line, g_text, word_count):
    last_index = len(g_text)
    found_index = line.find(g_text)

    if found_index != -1:
        first_part = line[:found_index].split()[-word_count:]
        last_part = line[found_index + last_index:].split()[:word_count]
        found_text = line[found_index:found_index + last_index]
        return ' '.join(first_part) + ' ' + found_text + ' ' + ' '.join(last_part)

    return None


def search_in_files(g_path, g_files, g_text, word_count, g_full):
    g_founds = collections.defaultdict(list)

    for file in g_files:
        file_path = os.path.join(g_path, file)
        str_count = 0

        for line in read_file(file_path):
            str_count += 1
            found_text = search_text_in_line(line, g_text, word_count)
            if found_text:
                g_founds[file].append((str_count, found_text))

                if not g_full:
                    return g_founds  # return if only first found is needed

    return g_founds


path, text, full = get_args()
files = get_files_with_extension(path, '.log')
founds = search_in_files(path, files, text, 5, full)


for key, found in founds.items():
    for str_num, found_str in found:
        print(f'Found in file: {key}\nLine number: {str_num}\n{found_str}\n')

    print(f'Total entries found in file "{key}": {len(found)}\n')
