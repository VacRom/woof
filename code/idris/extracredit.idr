module ec

import pair
import nat

data tree = empty | cons nat tree tree

e: tree
e = empty

obar: tree
obar = cons (S O) empty empty

t: tree
t = cons (S (S O)) obar (cons (S (S (S O))) empty empty)

count: tree -> nat
count empty = O
count (cons a b c) = S (addp (mkPair (count b) (count c)))
