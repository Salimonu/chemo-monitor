def calculate_bmi(weight, height):
    height_in_meter = height/100
    bmi = weight/(height_in_meter*height_in_meter)
    return bmi

