from fractions import Fraction

def view_data(data, title):
    print(f'{title} = {data}')

def get_value():
    return Fraction(input('value = '))