module bool

import pair
import bool
import nat

and: bool -> bool -> bool
and true true = true
and _ _ = false

or: bool -> bool -> bool
or true _ = true
or false n = n

xor: bool -> bool -> bool
xor true n = not n
xor false n = n

nand: bool -> bool -> bool
nand true n = not n
nand false _ = true

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
eq a b = and (isZero (sub a b) (isZero (sub b a)))


