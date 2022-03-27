import calculate_sum as calculate
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    calculate.init(value_a, value_b)
    result = calculate.do_it()
    view.view_data(result, 'result')