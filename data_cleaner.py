from read_csv import read
from filter_month import filtering


def month_dicts(data, month):

    januaruary ={}
    enero = {}
    febrero = {}
    marzo = {}
    abril = {}
    mayo = {}
    junio = {}
    julio = {}
    agosto = {}
    septiembre = {}
    octubre = {}
    noviembre = {}
    diciembre = {}

    for months in data:
        return months

    

if __name__ == '__main__':
    reader = read('data.csv')
    order = filtering(reader)
    print(month_dicts(order))