import numpy as np


# Version 1

# def slice_me(family: list, start: int, end: int) -> list:
#     if not (isinstance(i, list) for i in family):
#       try:
#           raise AssertionError("You can only provide 2D arrays!")
#       except AssertionError as e:
#     rows = len(family[0])
#     original_shape = [len(family), rows]
#     print("My original shape is: " + f"{original_shape}")
#     truncated_shape = family[start:end]
#     if (truncated_shape):
#         new_shape = [len(truncated_shape), len(truncated_shape[0])]
#     else:
#         new_shape[0, 0]
#     print ("My truncated shape is: " + f"{new_shape}")
#     return truncated_shape


# Version 2

# def slice_me(family: list, start: int, end: int) -> list:
#     """
#     Slice a 2D array
#     """
#     if not (isinstance(i, list) for i in family):
#        try:
#           raise AssertionError("You can only provide 2D arrays!")
#        except AssertionError as e:
#     rows = len(family[0])
#     original_shape = [len(family), rows]
#     print("My original shape is: " + f"{original_shape}")
#     truncated_shape = slice(start, end, 1)
#     new_shape = [start, end]
#     if (truncated_shape):
#         family[truncated_shape]
#     else:
#         family[0, 0]
#     print("My truncated shape is: ", new_shape)
#     return family[truncated_shape]


# Version 3 using numpy

def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D array
    """
    if not isinstance(family, list):
        try:
            raise AssertionError("You can only provide a list!")
        except AssertionError as e:
            return e
    if not all(len(i) == len(family[0]) for i in family):
        try:
            raise AssertionError("You can only provide 2D arrays!")
        except AssertionError as e:
            return e
    for i in family:
        if not all(isinstance(j, (int, float)) for j in i):
            try:
                raise AssertionError("You can only provide numbers!")
            except AssertionError as e:
                return e
    family = np.array(family)
    original_shape = family.shape
    print(f"My original shape is: {original_shape}")
    truncated_shape = family[start:end]
    new_shape = truncated_shape.shape
    print(f"My truncated shape is: {new_shape}")
    return truncated_shape.tolist()
