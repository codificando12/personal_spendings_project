from read_csv import read
from filter_month import filtering
from change_month_format import change_date_format
from excel_generator import create_excel_file


def run():
    spendings = read('./data.csv')
    month_format = change_date_format(spendings)
    january = filtering(month_format, 'Enero')
    february = filtering(month_format, 'Febrero')
    march = filtering(month_format, 'Marzo')
    april = filtering(month_format, 'Abril')
    may = filtering(month_format, 'Mayo')
    june = filtering(month_format, 'Junio')
    july = filtering(month_format, 'Julio')
    august = filtering(month_format, 'Agosto')
    september = filtering(month_format, 'Septiembre')
    october = filtering(month_format, 'Octubre')
    november = filtering(month_format, 'Noviembre')
    december = filtering(month_format, 'Diciembre')
    
    months_dicts = [january, february, march, april, may, june,
        july, august, september, october]
    
    excel_file = create_excel_file(months_dicts) 
    print(august)

if __name__ == '__main__':
    run()