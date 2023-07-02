from read_csv import read

def change_date_format(csv):

    
    for date_format in csv:
    
        if date_format['\ufeffDATE'].startswith('1/'):
            date_format['DATE'] = date_format.pop('\ufeffDATE')
            date_format['DATE'] = 'Enero'
        elif date_format['\ufeffDATE'].startswith('2'):
            date_format['DATE'] = date_format.pop('\ufeffDATE')
            date_format['DATE'] = 'Febrero'
        elif date_format['\ufeffDATE'].startswith('3/'):
            date_format['DATE'] = date_format.pop('\ufeffDATE')
            date_format['DATE'] = 'Marzo'
        elif date_format['\ufeffDATE'].startswith('4/'):
            date_format['DATE'] = date_format.pop('\ufeffDATE')
            date_format['DATE'] = 'Abril'
        elif date_format['\ufeffDATE'].startswith('5/'):
            date_format['DATE'] = date_format.pop('\ufeffDATE')
            date_format['DATE'] = 'Mayo'
        elif date_format['\ufeffDATE'].startswith('6/'):
            date_format['DATE'] = date_format.pop('\ufeffDATE')
            date_format['DATE'] = 'Junio'
        elif date_format['\ufeffDATE'].startswith('7/'):
            date_format['DATE'] = date_format.pop('\ufeffDATE')
            date_format['DATE'] = 'Julio'
        elif date_format['\ufeffDATE'].startswith('8/'):
            date_format['DATE'] = date_format.pop('\ufeffDATE')
            date_format['DATE'] = 'Agosto'
        elif date_format['\ufeffDATE'].startswith('9/'):
            date_format['DATE'] = date_format.pop('\ufeffDATE')
            date_format['DATE'] = 'Septiembre'
        elif date_format['\ufeffDATE'].startswith('10/'):
            date_format['DATE'] = date_format.pop('\ufeffDATE')
            date_format['DATE'] = 'Octubre'
        elif date_format['\ufeffDATE'].startswith('11/'):
            date_format['DATE'] = date_format.pop('\ufeffDATE')
            date_format['DATE'] = 'Noviembre'
        elif date_format['\ufeffDATE'].startswith('12/'):
            date_format['DATE'] = date_format.pop('\ufeffDATE')
            date_format['DATE'] = 'Diciembre'
        else:
            date_format['DATE'] = date_format.pop('\ufeffDATE')
            
    
    return csv


if __name__ == '__main__':
    file = read('./2022.csv')
    hola = (change_date_format(file))
    print(hola)
    