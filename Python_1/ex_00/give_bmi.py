def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate the BMI
    """
    bmi = []
    if not isinstance(height, list) or not isinstance(weight, list):
        print("The input must be a list!")
        exit(1)
    if len(height) != len(weight):
        print("The number of heights and weights must be equal!")
        exit(1)
    for j in range(len(height)):
        if isinstance(height[j], str):
            print("The input must be a number!")
            exit(1)
    for k in range(len(weight)):
        if isinstance(weight[k], str):
            print("The input must be a number!")
            exit(1)
    for i in range(len(height)):
        bmi.append(weight[i] / height[i] ** 2)
    return bmi


def apply_limit(bmi: list[int | float],
                limit: int | float) -> list[int | float]:
    """
    Apply a limit to a list of BMI values
    """
    if isinstance(bmi, list):
        return [True if b > limit else False for b in bmi]
    else:
        return True if bmi > limit else False
