module set

import list
import ite
import bool
import nat
import eq
import serialize

-- mkSet is meant to be private.
data set a = mkSet (list a)

-- a starting point for building any set
new_set: set a
new_set = mkSet nil

set_insert: (eq a) => a -> set a -> set a
set_insert v (mkSet l) = ite' (member v l) (mkSet l) (mkSet (v::l))

eql_set: (eq a) => set a -> set a -> bool
eql_set (mkSet x) (mkSet y) = and (subset_elements x y) (subset_elements y x)

instance (eq a) => eq (set a) where
  eql s1 s2 = eql_set s1 s2

--toStringListVal: set a -> String
--toStringListVal

--instance (serialize a) => serialize (set a) where
--  toString (mkSet l) = "{" ++ (toStringListVal l) ++ "}"
