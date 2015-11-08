import bool
import option
import pair
import list
import nat
import eq
import serialize

import list
import ite

import set_adt

-- Power Set

--ooo: (eq a) => set a -> set (set a)
--ooo (mkSet (h::t)) =

--bif: (eq a) => set a -> set (set a)
--bif (mkSet (h::nil)) = mkSet ((mkSet (h::nil))::nil)
--bif (mkSet (h::t)) = (mkSet ((mkSet (h::nil))::(mkSet t)::nil))^^(bif (mkSet t))

--bifurcate: (eq a) => set (set a) -> set (set a)
--bifurcate (mkSet (s1::s2::nil)) = (split s1)^^(split s2)

--powerset: (eq a) => set a -> set (set a)
--powerset s = bifurcate (split s)

--vvv: (eq a) => set (set a) -> set (set a)
--vvv = mkSet (v1::vt) = (mkSet (v1::nil))::(vvv (mkSet vt))

set1: set nat
set1 = mkSet ((S O)::(S (S O))::(S (S (S O)))::(S (S (S (S O))))::nil)

seta: set nat
seta = mkSet ((S O)::nil)

setb: set nat
setb = mkSet ((S (S O))::nil)

setc: set nat
setc = mkSet ((S (S (S O)))::nil)

set3: set (set nat)
set3 = mkSet (seta::setb::setc::nil)

set: set (set nat)
set = mkSet ((seta)::(mkSet nil)::nil)

set': set (set nat)
set' = (mkSet ((seta^^setb)::(seta)::nil))^^(mkSet ((setb)::(mkSet nil)::nil))

generate: (eq a) => set a -> nat -> set (set a)
generate s O = (mkSet ((mkSet nil)::nil))
generate s n = (generate s (sub n (S O)))^^(mkSet (s::nil))

order: (eq a) => set a -> set (set a)
order (mkSet nil) = (mkSet ((mkSet nil)::nil))
order s = generate s (exp (S (S O)) (set_cardinality s))


--bif: (eq a) => set (set a) -> set (set a)
--bif 

--split: a -> set (set a) -> set (set a)
--split 

--bif: set a -> set (set a) -> set (set a)
--bif (mkSet (h::t)) (mkSet (sh::st)) = mkSet (


 
 
 
