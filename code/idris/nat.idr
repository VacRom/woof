module nat

import bool
import eq
import serialize

data nat = O | S nat

isZero: nat -> bool
isZero O = true
isZero _ = false

evenb: nat -> bool
evenb O = true
evenb (S O) = false
evenb (S (S n)) = evenb n

oddb: nat -> bool
oddb x = not (evenb x)

add: nat -> nat -> nat
add O m = m
add (S n) m = S (add n m)

mult: nat -> nat -> nat
mult O m = O
mult (S n) m = add (mult n m) m

fact: nat -> nat
fact O = (S O)
fact (S n) = mult (S n) (fact n)

sub: nat -> nat -> nat
sub O m = O
sub n O = n
sub (S n) (S m) = sub n m

exp: nat -> nat -> nat
exp x O = (S O)
exp O x = O
exp x (S n) = mult x (exp x n)

le: nat -> nat -> bool
le O m = true
le (S n) O = false
le (S n) (S m) = le n m

eq: nat -> nat -> bool
eq a b = and (isZero (sub a b)) (isZero (sub b a))

gt: nat -> nat -> bool
gt a b = not (isZero (sub a b))

ge: nat -> nat -> bool
ge a b = or (eq a b) (gt a b)

lt: nat -> nat -> bool
lt a b = not (ge a b)

fib: nat -> nat
fib O = O
fib (S O) = (S O)
fib (S (S n)) = add (fib (S n)) (fib n)

eql_nat: nat -> nat -> bool
eql_nat O O = true
eql_nat (S n) O = false
eql_nat O (S m) = false
eql_nat (S n) (S m) = eql_nat n m

instance eq nat where
  eql n1 n2 = eql_nat n1 n2
  
instance serialize nat where
  toString O = "Z"
  toString (S n) = "s" ++ toString n
