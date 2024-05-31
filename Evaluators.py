import scipy.integrate as integrate
from Fix_Data import fix_data
from Predictors import*

def average_prob_compare(predictor, data, final_time=3600.0, exponent=1):
    fixed_data = fix_data(data)
    final_time = max(final_time, fixed_data[-1][0])
    if fixed_data[-1][1] > 0:
        w = 1
    elif fixed_data[-1][1] < 0:
        w = -1
    else:
        w = 0
    return w/final_time * integrate.quad(lambda t: (2*predictor(t, fixed_data, fixed=True, final_time=final_time) - 1)**exponent, 0, final_time)[0]

if __name__ == "__main__":
    from Examples import Chiefs_Bills_Jan_23_22
    print(average_prob_compare(first_to_score, Chiefs_Bills_Jan_23_22))