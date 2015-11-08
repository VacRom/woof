module list

import nat
import option
import bool
import ite
import eq
import serialize
import pair

infixr 7 ::,++ --This gives precedence/priority

data list a = nil | (::) a (list a)

length: list a -> Nat
length nil = 0
length (h :: t) = S (length t)

(++): list a -> list a -> list a
(++) nil b = b
(++) (h :: t) b = h :: t ++ b

map: (a -> b) -> list a -> list b
map f nil = nil
map f (h::t) = (f h)::(map f t)

-- Predicate of a -> Takes list a and returns a sublist of type list a.
filter: (a -> bool) -> list a -> list a
filter f nil = nil
filter f (h::t) = ite' (f h) -- IF
                      (h::(filter f t)) -- THEN
                          (filter f t) -- ELSE

filter': (a -> bool) -> list a -> list a
filter' f nil = nil
filter' f (h::t) = ite' (f h) (filter' f t) (h::(filter' f t))

foldr: (a -> a -> a) -> a -> (list a) -> a
foldr f id nil = id
foldr f id (h::t) = f h (list.foldr f id t)

head: (serialize a) => list a -> option a
head nil = none
head (h::t) = some h

tail: (serialize a) => list a -> option (list a)
tail nil = none
tail (h::t) = some t

member: (eq a) => a -> list a -> bool
member v nil = false
member v (h::t) = ite' (eql v h) true (member v t)

instance (eq a) => eq (list a) where
  eql nil nil = true
  eql (h::t) nil = false
  eql nil (h::t) = false
  eql (h1::t1) (h2::t2) =
    and (eql h1 h2) (eql t1 t2)

-- Is l1 contained in l2? We could have done this with member also.
subset_elements: (eq a) => list a -> list a -> bool
subset_elements nil _ = true
subset_elements a nil = false
subset_elements (h::t) (h'::t') = and (or (eql h h') (subset_elements (h::nil) t')) (subset_elements t (h'::t'))

toStringList: (serialize a) => list a -> String
toStringList nil = "]"
toStringList (h::nil) = (toString h) ++ "]"
toStringList (h::t) = (toString h) ++ "," ++ (toStringList t)

instance (serialize a) => serialize (list a) where
  toString l = "[" ++ (toStringList l)

-- How overloaded functions work: 
-- First read that toString is overloaded. Finds out which typeclass
-- instance is applied to this function (in this case, list a). Finds the
-- typeclass instance which is appropriate and its field. Takes this
-- field and applies it to our input. (Associates instance with a type)
