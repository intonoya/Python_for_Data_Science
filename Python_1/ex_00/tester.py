from give_bmi import give_bmi, apply_limit


height = [2.71, 1]
weight = [165.3, 25.5]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
