module text

ite: Integer -> a -> a -> a
ite 1 tb fb = tb
ite _ tb fb = fb

exist: String
exist = "Do you exist? For true or a positive reaction, respond with, myname 1. False or a negative reaction, myname 0."

myname: Integer -> String
myname n = ite n "Good.  How are you? (howis _)" "(exist)"

howis: Integer -> String
howis n = ite n "That is good. Are you in class? (inclass _)" "That is unfortunate. Any reason why? (reason _)"

inclass: Integer -> String
inclass n = ite n "Get a good grade. (thanks _)" "Hope you aren't late. (thanks _)"

reason: Integer -> String
reason n = ite n "I hope you feel better. (thanks _)" "I hope you feel better. (thanks _)"

thanks: Integer -> String
thanks n = ite n "Goodbye" "Goodbye"

-- Type in 'exist' to begin.
