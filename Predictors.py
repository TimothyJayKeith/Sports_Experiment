import numpy as np
from Fix_Data import fix_data

def first_to_score(t, data, fixed=False, final_time=3600.0):
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