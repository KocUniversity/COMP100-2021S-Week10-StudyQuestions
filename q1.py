def q1_a(i1, i2):

  items = [4, 5, 6, 8]
  result = items[i1] * items[i2]
  return result


def q1_b():

  names = ["apples" , "bananas", "grapes"]
  values = [5, 3, 7]

  for idx, name in enumerate(names):

    if name == "apples":
      return values[idx]
    else:
      return None


def q1_c():

  d = {"apples" : 5, "bananas": 3, "grapes": 7}

  return d["apples"]


def q1_d():

  """
  Finds and returns the maximum value inside a list
  """

  vector = [2,4,5,6]
  max_value = 0

  for item in vector:
    if item > max_value:
      max_value = item

  return max_value

def q1_e():

    """
    Finds and returns the maximum value inside nested two lists (like a matrix)
    """

    # Here we have a matrix, 2x4 (2 rows, 4 columns)

    matrix = [[2,4,5,6],
              [1,0,0,7]]

    max_value = 0
    for row in matrix:
      for item in row:
        if item > max_value:
          max_value = item

    return max_value


def q1_f():

    """
    Finds and returns the maximum value inside nested three lists (like a matrix)

    """

    # Here we have a matrix, 2x3x4 two matrices of (3 rows, 4 columns) ~ tensor.

    tensor =[[[2, 4, 5, 6],
              [1, 0, 9, 7],
              [2, 3, 4, 5]],

              [[5, 4, 5, 8],
              [2, 3, 3, 4],
              [7, 1, 1, 5]]]

    max_value = 0

    for matrix in tensor:
      for row in matrix:
        for item in row:
          if item > max_value:
            max_value = item

    return max_value


if __name__ == "__main__":
  print("A: ", q1_a(1,2))
  print("B: ", q1_b())
  print("C: ", q1_c())
  print("D: ", q1_d())
  print("E: ", q1_e())
  print("F: ", q1_f())

