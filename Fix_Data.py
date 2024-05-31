def fix_data(data, period_length=900.0):
    return[[(dpoint[0] - 1) * period_length + (15 - float(dpoint[1].split(":")[0])) * 60 - float(dpoint[1].split(":")[1])] + [dpoint[2] - dpoint[3]] for dpoint in data]