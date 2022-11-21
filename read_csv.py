import csv


def read(path):

    with open(path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            data_dic = {key: value for key, value in iterable}
            data.append(data_dic)

        print(data)
if __name__ == '__main__':
    read('./data.csv')