# Exercise: Stack

'''
1. Write a function in python that can reverse a string using stack data structure.
   Use `5_stack.ipynb` from the tutorial.

    reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
'''
from collections import deque


def reverse_string(str):
    reversed = ""
    stack = deque()
    stack.extend(str)
    l = len(stack)
    while l != 0:
        reversed += stack.pop()
        l -= 1
    return reversed


r1 = reverse_string("hello")
print(f"reverse string of hello: {r1}")
r2 = reverse_string("We will conquere COVID-19")
print(f"reverse string of We will conquere COVID-19: {r2}")

'''
2. Write a function in python that checks if paranthesis in the string are balanced or not.
   Possible parantheses are "{}',"()" or "[]".
   Use `5_stack.ipynb` from the tutorial.
    
    is_balanced("({a+b})")     --> True
    is_balanced("))((a+b}{")   --> False
    is_balanced("((a+b))")     --> True
    is_balanced("))")          --> False
    is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
    
'''


def is_match(chr):
    dict = {'}': '{', ']': '[', ')': '('}
    return dict[chr]


def is_balanced(str):
    stack = deque()
    for chr in str:
        if chr in "{([":
            stack.append(chr)
        if chr in "})]":
            if len(stack) == 0 or is_match(chr) != stack.pop():
                return False
    return len(stack) == 0
    """
    # first solution I wrote has a problem
    # it doesn't consider when it has equal number of parenthese each side but not the wrong one
    # {[}] --> gives me True, which is False indeed
    stack = deque()
    for chr in str:
        if chr in "{([":
            stack.append(chr)
        if chr in "})]":
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack) == 0
    """


print("is_balanced(\"({a+b}))\"): " + str(is_balanced("({a+b})")))
print("is_balanced(\"))((a+b}{\"): " + str(is_balanced("))((a+b}{")))
print("is_balanced(\"((a+b))\"): " + str(is_balanced("((a+b))")))
print("is_balanced(\"))\"): " + str(is_balanced("))")))
print("is_balanced(\"[a+b]*(x+2y)*{gg+kk}\") : " +
      str(is_balanced("[a+b]*(x+2y)*{gg+kk}")))

print("is_balanced(\"({a+b)})\"): " + str(is_balanced("({a+b)}")))
