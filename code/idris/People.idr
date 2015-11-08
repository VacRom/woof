module People

import Person
import bool
import list

tom: Person
tom = MkPerson "Tom" 19 5 5 5 5 5 5 5 false

mary: Person
mary = MkPerson "Mary" 20 1 2 3 4 5 6 7 true

ge: Person
ge = MkPerson "Ge" 21 7 6 5 4 3 2 1 true

daryl: Person
daryl = MkPerson "Daryl" 19 7 7 7 7 7 7 7 false

people: list Person
people = tom::
         mary::
         ge::
         daryl::
         nil

-- Note that this is surjective, but not necessarily
  -- injective. Therefore the mapping is not always bijective. Thus
  -- the cardinality of the sets may not be the same.
mapAge: list Person -> list Nat
mapAge nil = nil
mapAge (h::t) = (age h)::(mapAge t)

--oneLine: Nat
--oneLine = list.foldr plus 0 (map age (filter gender people))

--query: (value -> result -> result) -> result -> (tuple -> value) ->
  --(tuple -> bool) -> (list tuple) -> result
  
