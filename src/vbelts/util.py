"""Utilities"""

import csv
import os

class OutOfRangeError(Exception):
    """Raised when value is out of range of the list"""
    pass

class NotValidError(Exception):
    """Raised when the value passed to the function is not valid"""


def _read_csv_data_list(filename:str):
    # use the full path and pass the file path as filename
    file_path = os.path.join(os.path.dirname(__file__), 'data', filename)
    li_result = []
    with open(f'{file_path}.csv', mode='r') as csv_file:
        reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        next(reader)
        for line in reader:
            li_result.append(line)
        return li_result

def _read_csv_data(filename:str):
    # use the full path and pass the file path as filename
    file_path = os.path.join(os.path.dirname(__file__), 'data', filename)  # fetch full path
    with open(f'{file_path}.csv', mode='r') as csv_file:
        reader = csv.DictReader(csv_file, quoting=csv.QUOTE_NONNUMERIC)  # not quoted values are floats
        # next(reader)
        for line in reader:
            yield line


def _interpol(x_data:float, x_min:float, x_max:float, y_min:float, y_max:float):
    """Linear interpolation of the table data

    Args:
        x_data (float): desired input data point
        x_min (float): nearest minimum input value in relation to the data point
        x_max (float): nearest maximum input value in relation to the data point
        y_min (float): nearest minimum output value in the relation to the data point
        y_max (float): nearest maximum output value in the relation to the data point
    
    Results:
        float: interpolated output value"""
    return y_max-((x_max - x_data)/(x_max - x_min))*(y_max - y_min)

def _min_dist(x:float, x_min:float, x_max:float):
    """Returns the nearest value between two items, given one item that is in the interval of the two

    Args:
        x (float): desired value for calculation
        x_min (float): nearest minimum value on the scale
        x_max (float): nearest maximum value on the scale
    
    Returns:
        float: nearest value of x"""
    dist_1 = (x - x_min)/x
    dist_2 = (x_max - x)/x
    if dist_1 < dist_2:
        return x_min
    elif dist_1 > dist_2:
        return x_max
    elif dist_1 == dist_2: # if both are equal, return the maximum
        return x_max
    else:
        raise ValueError

def gear_ratio(input_pulley:float, output_pulley:float):
    """Calculates the gear ratio

    Args:
        input pulley (float): input (drive) pulley diameter
        output pulley (float): output (driven) pulley diameter
    
    Returns:
        float: gear ratio"""
    if isinstance(input_pulley, (float, int)) and isinstance(output_pulley, (float, int)):
        return output_pulley/input_pulley
    else:
        raise ValueError


def est_power(engine_power:float, serv_factor:float):
    """Calculates the estimated power to run the pulley system

    Args:
        engine_power (float): engine power, hp
        serv_factor (float): calculated service factor, use vbelts.service_factor()
    
    Returns:
        float: estimated power, hp"""
    if isinstance(engine_power, (float, int)) and isinstance(serv_factor, (float, int)):
        return engine_power * serv_factor
    else:
        raise ValueError
