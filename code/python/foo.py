# {} This is the state of the execution.
print("")
x = 5
# { (x,5) }
print("x=")
print (x)
# { (x,5) }
x = 6
# { (x,6) }
print("x=")
print(x)
# { (x,6) }
y = 7# this is a tuple overwrite
# { (x,6) , (y,7) } All values are stored as tuples. I.e (x,6).
print("x=")
print(x)
print("y=")
print(y)
# x gets 6. Assignment state.

x = 99
print(1000*x*x)

# State

# Arithmetic expression: 1+2
# Boolean expression: 1>2 => F
# Procedure (function) call: print(1+2)
# Note that procedures in imperative languages can write languages
# into files.

# Commands
# Assignment: variable = expression. "variable gets an expression and
# stores it"
# Conditional: if (boolean expression) (command for true) (command for
# false)
# Iteration: while (boolean expression command)
# Procedure call: can appear in code or typed in manually
# Composition: command;command

p = ("Sally",69,15,True)

# p[0] = "Sally"
# p[1] = "69"

# Dictionary
d = { "x" : 5, "y" : 7}
print(d["x"])

# Function is 1-1. Else relation.
