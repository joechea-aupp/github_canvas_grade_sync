import os
# list files in the current directory that has extention .csv


def list_csv() -> list:
    csv_list = []
    for file in os.listdir():
        if file.endswith('.csv'):
            csv_list.append(file)

    return csv_list
