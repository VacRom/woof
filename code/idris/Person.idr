module Person

import bool

||| A record type that is equivalent to:
||| (data Person = mkPerson String nat)
||| but where we give names to fields.
||| A person has a name and an age in
||| years.
record Person where
    constructor MkPerson
    name : String
    age : Nat
    strength : Nat
    perception: Nat
    endurance: Nat
    charisma: Nat
    intelligence: Nat
    agility: Nat
    luck: Nat
    trustworthy: bool
    
-- An example value of type Person
AvGuy: Person
AvGuy = MkPerson "AverageGuy"  20 5 5 5 5 5 5 5 true

-- And now here's the key idea: The
-- names of the fields are automatically
-- names of projection functions! Here
-- we get out the age of person, p.

n: String
n = name AvGuy
-- expect "AvGuy"

y: Nat
y = age AvGuy
-- expect 3

s: Nat
s = strength AvGuy
-- expect 5

-- And so on...

----------- How to do it the long way ------------------
-- ("getters")
getName': Person -> String
getName' (MkPerson a b c d e f g h i j) = a

-- field override functions ("setters")
setName': Person -> String -> Person
setName' (MkPerson a b c d e f g h i j) a' = (MkPerson a' b c d e f g h i j)

----------- How to do it the better way ----------------
-- Type in: age AvGuy to return 20

setName: Person -> String -> Person
setName p n = record { name = n } p

-- This is possible because we defined our record types already.
