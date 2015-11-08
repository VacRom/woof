module dna

import list
import pair
import bool
import ite

infixr 7 ::

data base = A | T | C | G
data basePair = nil | (::) (pair base base) (list (pair base base))

complement_base: base -> base
complement_base A = T
complement_base T = A
complement_base C = G
complement_base _ = C

complement_strand: list base -> list base
complement_strand nil = nil
complement_strand (h::t) = map (complement_base) (h::t)

-- Do we really need to use mkPair? Given one strand of DNA we have
  -- all the information needed to write out either strands since they
  -- are always complements of one another.
  -- In other words, list base gives the exact same information as
  -- list (mkPair base base) [the only exception is knowing which
  -- strand is '1st' and '2nd' but this can be chosen arbitrarily].

--strand1: list base -> list base
--strand1 nil = nil
--strand1 (h::t) = h::(strand1 t)

--strand2: list base -> list base
--strand2 nil = nil
--strand2 (h::t) = (complement_base h)::(strand2 t)

strand1: list (pair base base) -> list base
strand1 nil = nil
strand1 ((mkPair h h')::t) = h::(strand1 t)

strand2: list (pair base base) -> list base
strand2 nil = nil
strand2 ((mkPair h h')::t) = h'::(strand2 t)

-- Easily done when we write the function pairUp
pairUp: base -> pair base base
pairUp a = (mkPair a (complement_base a))

complete: list base -> list (pair base base)
complete nil = nil
complete (h::t) = (map (pairUp) (h::t)) -- [A,T,C,G] -> [AT,TA,CG,GC]

-- We can also write this without map when we make the right hand
  -- side: (mkPair h (complement_base h))::complete(t)

-- NOTE on this last question I know that I have to be able to make a
  -- universal function for a given base type b, but I'm not able to
  -- get Idris to compile it. So for the meanwhile, I wrote out four
  -- cases specifically for each base type which does complie and
  -- correctly does what we want, using map and foldr.

-- [C,T,A,G,A] -> [0,0,1,0,1] -> foldr

check: base -> base -> bool
check A A = true
check T T = true
check C C = true
check G G = true
check _ _ = false

base2bool: base -> base -> bool
base2bool a b = ite' (check a b) true false

convert: list base -> base -> list bool
convert nil a = nil
convert (h::t) b = (list.map (base2bool b) (h::t))

reduce: list bool -> list bool
reduce nil = nil
reduce (h::t) = filter (bool.id) (h::t)

counting: list bool -> Nat
counting nil = 0
counting (h::t) = length (h::t)

countBase: base -> list base -> Nat
countBase a nil = 0
countBase b (h::t) = counting (reduce (convert (h::t) b))
