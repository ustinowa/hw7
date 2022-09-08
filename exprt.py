def write_file_1(path='phone1.csv'):
    import csv

    filename = "phone1.csv"

    phone = [
        ['Ivanov\n', 'Ivan\n', '(777)777-77-77\n', 'Desc\n'],
        ['Smirnov\n', 'Pavel\n', '(999)999-99-99\n', 'Desc\n']
    ]

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(phone)

    return path


def write_file_2(path='phone2.csv'):
    import csv

    filename = 'phone2.csv'

    phone = [
        ['Ivanov', 'Ivan', '(777)777-77-77', 'Desc'],
        ['Smirnov', 'Pavel', '(999)999-99-99', 'Desc']
    ]

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(phone)

    return path
