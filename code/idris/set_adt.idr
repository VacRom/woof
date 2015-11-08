module set_spec

import bool
import option
import pair
import list
import nat
import eq
import serialize

import list
import ite

infixr 7 ^^

data set: (a: Type) -> Type
data set a = mkSet (list a)

--*******Specifications

-- The empty set.
emptySet: (eq a) => set a -- Identify type as as "emptySet {a = "type'}"

-- The set, s, is empty => true, else false.
isEmpty: set a -> bool

-- S u {v}
set_insert: (eq a) => a -> set a -> set a

-- S \ {v}
set_remove: (eq a) => a -> set a -> set a

-- |S|
set_cardinality: (eq a) => set a -> nat

-- v element S => true, else false
set_member: (eq a) => a -> set a -> bool

-- S_1 u S_2
set_union: (eq a) => set a -> set a -> set a

-- S_1 n S_2
set_intersection: (eq a) => set a -> set a -> set a

-- S_1 \ S_2
set_difference: (eq a) => set a -> set a -> set a

-- A function p is true A (for all) S => true, else false.
set_forall: (a -> bool) -> set a -> bool

-- E (there exists) p for some a element S => true, else false.
set_exists: (a -> bool) -> set a -> bool

-- E p, a element S => some a, else none
set_witness: (a -> bool) -> set a -> option a

-- For a and b <=> (a,b), Cartesian product.
set_product: set a -> set b -> set (pair a b)

-- S_1 = S_2 => true, else false.
set_eql: (eq a) => set a -> set a -> bool
-- ;; HOWEVER, you should simply use eql.

-- S_1 => "S_1"
set_toString: (serialize a) => set a -> String
-- ;; HOWEVER, you should simply use toString.

--*******Implelmentations

-- This is similar to append (++) but for sets.
(^^): (eq a) => set a -> set a -> set a
(^^) (mkSet nil) s = s
(^^) (mkSet (h::t)) (mkSet b) = (mkSet (h::t++b))

-- We must identify the type a as "emptySet {a = 'type'}",
  -- i.e. "emptySet {a = bool}".
emptySet = mkSet nil

-- Let's make a checker function that takes a set with possibly
-- repeated elements to a set without repeated elements. This will be helpful later.
checker: (eq a) => set a -> set a
checker (mkSet nil) = (mkSet nil)
checker (mkSet (h::t)) = ite' (member h t) (checker (mkSet t)) ((mkSet (h::nil))^^(checker (mkSet t)))

isEmpty (mkSet nil) = true
isEmpty _ = false

set_insert v (mkSet l) = ite' (member v l) (checker( mkSet l)) (checker (mkSet (v::l)))

set_remove v (mkSet nil) = (mkSet nil)
set_remove v (mkSet (h::t)) = checker (mkSet (filter' (eql v) (h::t)))

-- Annoying, but we switched our length function from nat to Nat. Make
-- length' for nat.

length': list a -> nat
length' nil = O
length' (h::t) = S (length' t)

unSet: set a -> list a
unSet (mkSet nil) = nil
unSet (mkSet l) = l

set_cardinality (mkSet nil) = O
set_cardinality s = length' (unSet (checker s))

set_member v (mkSet nil) = false
set_member v (mkSet (h::t)) = or (eql v h) (set_member v (mkSet t))

set_union (mkSet nil) (mkSet nil) = (mkSet nil)
set_union s1 s2 = checker (s1^^s2)

set_intersection a (mkSet nil) = (mkSet nil)
set_intersection (mkSet nil) b = (mkSet nil)
set_intersection (mkSet (h1::t1)) (mkSet l2) = checker (ite' (member h1 l2) ((mkSet (h1::nil))^^(set_intersection (mkSet t1) (mkSet l2))) (set_intersection (mkSet t1) (mkSet l2)))

set_difference a (mkSet nil) = a
set_difference (mkSet nil) b = (mkSet nil)
set_difference (mkSet (h1::t1)) (mkSet l2) = checker (ite' (member h1 l2) (set_difference (mkSet t1) (mkSet l2)) (mkSet (h1::nil))^^(set_difference (mkSet t1) (mkSet l2)))

set_forall p (mkSet nil) = true
set_forall p (mkSet (h::t)) = and (p h) (set_forall p (mkSet t))

set_exists p (mkSet nil) = false
set_exists p (mkSet (h::t)) = or (p h) (set_exists p (mkSet t))

answer: (a -> bool) -> set a -> a
answer p (mkSet (h::t)) = ite' (p h) (h) (answer p (mkSet t))

set_witness p s = ite' (set_exists p s) (some (answer p s))(none)

pairelt: a -> list b -> list (pair a b)
pairelt someA nil = nil
pairelt someA (b::tb) = (mkPair someA b)::(pairelt someA tb)

pairlist: list a -> list b -> list (pair a b)
pairlist nil l2 = nil
pairlist (h::t) l2 = (pairelt h l2)++(pairlist t l2)

set_product (mkSet s1) (mkSet s2) = mkSet (pairlist s1 s2)

-- Return set of all sets element s, of order 2^n.
--set_powerset: (s: set a) -> set (set a)
--set_powerset s = permutate (separate s)

-- A subset B?
set_contain: (eq a) => set a -> set a -> bool
set_contain (mkSet nil) s2 = true
set_contain (mkSet (h1::t1)) (mkSet l2) = and (member h1 l2) (set_contain (mkSet t1) (mkSet l2))

set_eql (mkSet nil) s2 = true
set_eql s1 s2 = and (set_contain s1 s2) (set_contain s2 s1)

set_toString (mkSet nil) = "}"
set_toString (mkSet (h::nil)) = (toString h) ++ "}"
set_toString (mkSet (h::t)) = (toString h) ++ "," ++ (set_toString (mkSet t))

instance (eq a) => eq (set a) where
  eql s1 s2 = set_eql s1 s2

instance (serialize a, eq a) => serialize (set a) where
  toString s = "{" ++ (set_toString (checker s))
