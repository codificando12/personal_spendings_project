from read_csv import read

def change_date_format(csv):

    
    for date_format in csv:
    
        if date_format['\ufeff"DATE"'].startswith('1/'):
            date_format['DATE'] = date_format.pop('\ufeff"DATE"')
            date_format['DATE'] = 'Enero'
        elif date_format['\ufeff"DATE"'].startswith('2'):
            date_format['DATE'] = date_format.pop('\ufeff"DATE"')
            date_format['DATE'] = 'Febrero'
        elif date_format['\ufeff"DATE"'].startswith('3/'):
            date_format['DATE'] = date_format.pop('\ufeff"DATE"')
            date_format['DATE'] = 'Marzo'
        elif date_format['\ufeff"DATE"'].startswith('4/'):
            date_format['DATE'] = date_format.pop('\ufeff"DATE"')
            date_format['DATE'] = 'Abril'
        elif date_format['\ufeff"DATE"'].startswith('5/'):
            date_format['DATE'] = date_format.pop('\ufeff"DATE"')
            date_format['DATE'] = 'Mayo'
        elif date_format['\ufeff"DATE"'].startswith('6/'):
            date_format['DATE'] = date_format.pop('\ufeff"DATE"')
            date_format['DATE'] = 'Junio'
        elif date_format['\ufeff"DATE"'].startswith('7/'):
            date_format['DATE'] = date_format.pop('\ufeff"DATE"')
            date_format['DATE'] = 'Julio'
        elif date_format['\ufeff"DATE"'].startswith('8/'):
            date_format['DATE'] = date_format.pop('\ufeff"DATE"')
            date_format['DATE'] = 'Agosto'
        elif date_format['\ufeff"DATE"'].startswith('9/'):
            date_format['DATE'] = date_format.pop('\ufeff"DATE"')
            date_format['DATE'] = 'Septiembre'
        elif date_format['\ufeff"DATE"'].startswith('10/'):
            date_format['DATE'] = date_format.pop('\ufeff"DATE"')
            date_format['DATE'] = 'Octubre'
        elif date_format['\ufeff"DATE"'].startswith('11/'):
            date_format['DATE'] = date_format.pop('\ufeff"DATE"')
            date_format['DATE'] = 'Noviembre'
        elif date_format['\ufeff"DATE"'].startswith('12/'):
            date_format['DATE'] = date_format.pop('\ufeff"DATE"')
            date_format['DATE'] = 'Diciembre'
        else:
            date_format['DATE'] = date_format.pop('\ufeff"DATE"')
            
    
    return csv


if __name__ == '__main__':
    file = read('./data.csv')
    hola = (change_date_format(file))
    print(hola)
    