## Study Questions:

### Q1) Analyzing algorithms

Analyze the functions and the docstrings in *q1.py*.

Write down algorithmic complexities (in Big-O Notation) of these as a comment and explain it why.

Think about the worst case scenarios and make comments on these. For example, in which cases you prefer dictionaries over lists?

### Your answers:

* q1_a: 

* q1_b:

* q1_c:

* q1_d:

* q1_e:

* q1_f:



### Q2) Intern's Quest: Fibonacci with Mathematicians

**Use the template file: q2.py**

Our intern from last time finishes his internship at the health center and decides to do another internship at the Math department by working at Prof. AsksAlot's lab. 

1. On his first day, Prof. AsksAlot asks the intern to come up with a solution to check whether a number is a Fibonacci number or not. Prof. AsksAlot also tells the intern, she will have a list of numbers (queries) to check where the size of the list is M. 

The function will return `True` for any number in the sequence of Fibonacci numbers below and `False` otherwise.

> 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

(Note the initial values of the Fibonacci series.)

The intern remembers from his COMP100 course that there is an efficient solution to Fibonacci by storing intermediate values in a dictionary:

```
def fib_efficient(n, d): 
  if n in d:
    return d[n] 
  else:
    ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
    d[n] = ans
  return ans
```

The intern assumes that he will be given a number `n_max` as an argument to set the maximum limit on the query number. By using the `fib_efficient` above, he computes the set of Fibonacci numbers up to the `n_max`'th Fibonnaci number, stores them in the dictionary `d`. Then, for each number in the list of queries, he looks into the dictionary to check if that number is a Fibonacci number or not. Note that keys in the dictionary hold the indices of Fibonacci numbers, corresponding values contain the actual number.

Implement the `check_fibonacci(queries, d)` function where `queries` is a list of numbers that we want to query and `d` is the dictionary that was created using the `fib_efficient` function. Your function should return a boolean list of size M where the i'th element in that list is `True` if the i'th number in the `queries` list is a Fibonacci number, and `False` otherwise.

Ignoring the creation of the dictionary which is done only once at the beginning, what is the time complexity of the intern's solution for a list of M numbers to check? 

2. Prof. AsksAlot listens to intern's solution but she is not impressed. She thinks that requiring `n_max` as an argument is a limitation and she can think of a better solution for two more reasons, at least. 

She is surprised that the intern has not heard of the *perfect square* rule for Fibonacci numbers:

> A number x is a Fibonacci number if and only if one or both of (5\*x^2 + 4) or (5\*x^2 – 4) is a [perfect square] (https://en.wikipedia.org/wiki/Fibonacci_number#Identification). 

To check if a number is a perfect square, one can:
  1. take its square root by using the `sqrt` function of Python's `math` module,
  2. cast it into int,
  3. take the square of the int,
  4. compare it to the original number.

Now, the intern who is slightly regretting taking that internship, is asked to implement the check using the perfect square rule. Implement the new solution for the poor intern and comment on the time complexity of it. 

Implement the `check_fibonacci_clever(queries)` function. Similar to the previous part, `queries` is a list of numbers that we want to query. Your function should return a boolean list of size M where the i'th element in that list is `True` if the i'th number in the `queries` list is a Fibonacci number, and `False` otherwise.

In addition to getting rid of `n_max`, what could be the other **two reasons** for Prof. AsksAlot to prefer this solution over the intern's solution, besides the fact that math is beautiful and everyone should know and use perfect squares?

**Hint**: Prof. AsksAlot plans to deploy the final algorithm on a small chip with limited memory.