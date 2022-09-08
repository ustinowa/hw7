def read_file_1(path='phone1.csv'):
    import csv

    filename = "phone1.csv"

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0], row[1], row[2], row[3])

    return path


def read_file_2(path='phone2.csv'):
    import csv

    filename = "phone2.csv"

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0], ',', row[1], ',', row[2], ',', row[3])

    return path
