import numpy as np
import scipy.integrate as integrate
from datetime import datetime

def fix_data(data):
    return[[(dpoint[0] - 1) * 900.0 + (15 - float(dpoint[1].split(":")[0])) * 60 - float(dpoint[1].split(":")[1])] + [dpoint[2] - dpoint[3]] for dpoint in data]

def first_to_score(data, t, fixed=False, final_time=3600.0):
    if not fixed:
        fixed_data = fix_data(data)
    else:
        fixed_data = data
    first_score = fixed_data[0][0]
    if t < first_score:
        return 0.5
    if t >= first_score and fixed_data[0][1] > 0:
        return 1.0
    if t >= first_score and fixed_data[0][1] < 0:
        return 0.0

def average_prob_compare(predictor, data, final_time=3600.0):
    fixed_data = fix_data(data)
    final_time = max(final_time, fixed_data[-1][0])
    if fixed_data[-1][1] > 0:
        w = 1
    elif fixed_data[-1][1] < 0:
        w = -1
    else:
        w = 0
    return w/final_time * integrate.quad(lambda t: predictor(fixed_data, t, fixed=True, final_time=final_time) - .5, 0, final_time)[0]

if __name__ == "__main__":
    from Examples import Chiefs_Bills_Jan_23_22
    print(average_prob_compare(first_to_score, Chiefs_Bills_Jan_23_22))