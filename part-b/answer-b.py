from propositional_logic import *

A = BoolVar('A')
B = BoolVar('B')
C = BoolVar('C')

# write code using A, B, and C, along with 
# the classes from propositional_logic.py
# and the .format() mathod to output the
# following expression:

# (((A => B) & (B => C)) => (A => C))

f_left = And(Implies(A, B), Implies(B, C))
f_right = Implies(A, C)
f = Implies(f_left, f_right)

print(f.format())

