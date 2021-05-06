import math 

def fib_efficient(n, d): 
  if n in d:
    return d[n] 
  else:
    ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
    d[n] = ans

  return ans


def check_fibonacci(queries, d):
  ##########################
  ### START OF YOUR CODE ###
  ##########################



  ##########################
  ###  END OF YOUR CODE  ###
  ########################## 
  pass


'TIME COMPLEXITY OF check_fibonacci function:'
'ENTER YOUR SOLUTIONS AS A COMMENT.'

############################
### START OF YOUR ANSWER ###
############################
#
#
#
#
#
############################
###  END OF YOUR ANSWER  ###
############################


def check_fibonacci_clever(queries):
  ##########################
  ### START OF YOUR CODE ###
  ##########################



  ##########################
  ###  END OF YOUR CODE  ###
  ########################## 
  pass


'TIME COMPLEXITY OF check_fibonacci_clever:'
'ENTER YOUR SOLUTIONS AS A COMMENT.'

############################
### START OF YOUR ANSWER ###
############################
#
#
#
############################
###  END OF YOUR ANSWER  ###
############################


'TWO REASONS WHY THE SECOND METHOD IS BETTER:'
'ENTER YOUR ANSWER AS A COMMENT'

############################
### START OF YOUR ANSWER ###
############################
#
# 1.
# 2.
#
############################
###  END OF YOUR ANSWER  ###
############################


if __name__ == "__main__":
  # n_max is required for the first solution
  n_max = 40
  d = None

  ##########################
  ### START OF YOUR CODE ###
  ##########################

  # initialize the dictionary as explained with the frst two values in the seq
  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...


  # call fib_efficient
  # only done once at the beginning


  # now d must contain all the Fibonnacci numbers up to n_max'th Fibonnaci number
  print("dictionary d: ")
  print(d)

  ##########################
  ###  END OF YOUR CODE  ###
  ########################## 

  # list of queries
  queries = [55, 8, 5, 22, 987, 134, 2584, 317811, 514299, 6765, 375, 528]

  print("Answers with Method1:")
  print(check_fibonacci(queries, d))
  
  print("Answers with Method2:")
  print(check_fibonacci_clever(queries))
  
  #BOTH OF YOUR OUTPUTS SHOULD BE:
  #[True, True, True, False, True, False, True, True, False, True, False, False]