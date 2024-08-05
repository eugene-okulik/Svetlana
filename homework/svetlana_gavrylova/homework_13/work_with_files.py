import os
import datetime


def parse_data_from_file(f_path):
    num_date_dict = {}

    with open(f_path, 'r') as data_file:
        for line in data_file.readlines():
            num_res, date_res = extract_number_date(line)
            num_date_dict[num_res] = date_res
        return num_date_dict


def extract_number_date(line):
    number_end_index = line.index('. ')
    number = int(line[:number_end_index])

    date_start_index = number_end_index + 2
    date_end_index = line.index(' -')
    date_string = line[date_start_index:date_end_index]
    # 2023-12-04 20:34:13.212967
    format_date = '%Y-%m-%d %H:%M:%S.%f'
    date_res = datetime.datetime.strptime(date_string, format_date)

    return number, date_res


def add_week(expected_date):
    return expected_date + datetime.timedelta(weeks=1)


def day_of_week(expected_date):
    return expected_date.strftime('%A')


def days_ago(expected_date):
    return (datetime.datetime.now() - expected_date).days


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

date_operations = {
    1: add_week,
    2: day_of_week,
    3: days_ago
}

formated_data = parse_data_from_file(file_path)
for num, date in formated_data.items():
    print(date_operations[num](date))
