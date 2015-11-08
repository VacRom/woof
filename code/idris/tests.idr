-- Here are tests for bool, nat, and list_nat

import unit
import bool
import nat
import pair
import option
import list
import serialize
import eq

import People

-- unit.idr tests

unittest: unit -> unit
unittest mkUnit = mkUnit -- mkUnit

serializeUnit: String
serializeUnit = toString mkUnit -- "()"

-- bool.idr tests

idTest1: bool
idTest1 = bool.id true -- true

idTest2: bool
idTest2 = bool.id false -- false

constFalseTest1: bool
constFalseTest1 = constFalse true -- false

constFalseTest2: bool
constFalseTest2 = constFalse false -- false

constTrueTest1: bool
constTrueTest1 = constTrue true -- true

constTrueTest2: bool
constTrueTest2 = constTrue false -- true

notT: bool
notT = not true -- false

notF: bool
notF = not false -- true

andTT: bool
andTT = and true true -- true

andTF: bool
andTF = and true false -- false

-- for the sake of space, since we know that TF and FT will produce
  -- the same results, we shall only test for one of the cases for
  -- each of the functions.
  
andFF: bool
andFF = and false false -- false

orTT: bool
orTT = or true true -- true

orTF: bool
orTF = or true false -- true

orFF: bool
orFF = or false false -- false

xorTT: bool
xorTT = xor true true -- false

xorTF: bool
xorTF = xor true false -- true

xorFF: bool
xorFF = xor false false -- false

nandTT: bool
nandTT = nand true true -- false

nandTF: bool
nandTF = nand true false -- true

nandFF: bool
nandFF = nand false false -- true

serializeBool: String
serializeBool = toString true -- "True"

-- nat.idr tests

isZeroO: bool
isZeroO = isZero O -- true

isZeroS: bool
isZeroS = isZero (S O) -- false

addTest1: nat
addTest1 = add O (S O) -- (S O)

addTest2: nat
addTest2 = add (S O) O -- (S O)

addTest3: nat
addTest3 = add (S O) (S O) -- (S (S O))

multTest1: nat
multTest1 = mult O (S O) -- O

multTest2: nat
multTest2 = mult (S O) O -- O

multTest3: nat
multTest3 = mult (S O) (S (S O)) -- (S (S O))

factTest1: nat
factTest1 = fact O -- (S O)

factTest2: nat
factTest2 = fact (S O) -- (S O)

factTest3: nat
factTest3 = fact (S (S (S O))) -- (S (S (S (S (S (S O))))))

subTest1: nat
subTest1 = sub O (S O) -- O

subTest2: nat
subTest2 = sub (S O) O -- (S O)

subTest3: nat
subTest3 = sub (S (S (S O))) (S O) -- (S (S O))

expTest1: nat
expTest1 = exp (S O) O -- (S O)

expTest2: nat
expTest2 = exp O (S O) -- O

expTest3: nat
expTest3 = exp O O -- (S O)

expTest4: nat
expTest4 = exp (S (S (S O))) (S (S O)) -- (S O) x 9

-- Tests for inequalities are simple. Test for when a<b, a=b, and
  -- a>b. All inequalities have been tested for correctness with these
  -- three tests (redundant to write out all of them, I shall do le as
  -- an example).
  
leTest1: bool
leTest1 = le O (S O) -- true

leTest2: bool
leTest2 = le (S O) O -- false

leTest3: bool
leTest3 = le (S O) (S O) -- true

fibTest1: nat
fibTest1 = fib O -- O

fibTest2: nat
fibTest2 = fib (S O) -- (S O)

fibTest3: nat
fibTest3 = fib (S (S (S (S O)))) -- (S (S (S O)))

serializeNat: String
serializeNat = toString (S (S (S O))) -- "sssZ"

-- pair.idr tests

pair1: pair bool bool
pair1 = (mkPair true false)

pairTestF: bool
pairTestF = fst pair1 -- true

pairTestS: bool
pairTestS = snd pair1 -- false

-- option.idr tests

op1: option bool
op1 = none

op2: option bool
op2 = some true

op3: option unit
op3 = some mkUnit

-- list.idr tests

-- {5,6,7}
list3: list Nat
list3 = 5 :: 6 :: 7 :: nil

-- {1,2,3}
list4: list Nat
list4 = 1 :: 2 :: 3 :: nil

lengthTest3: Nat
lengthTest3 = list.length list3 -- 3

lengthTest4: Nat
lengthTest4 = list.length list4 -- 3

appendTest: list Nat
appendTest = list3 ++ list4 -- {5,6,7,1,2,3}

constant: Nat -> Nat
constant a = 0

mapTest: list Nat -> list Nat
mapTest nil = nil
mapTest (h::t) = (constant h) :: (mapTest t)
-- maps {5,6,7}->{0,0,0}
-- equivalently...
mapTest2: list Nat
mapTest2 = list.map constant list3 -- {0,0,0}

labTest1: list bool
labTest1 = map evenb (O::(S O)::(S (S O))::(S (S (S (S O))))::nil)

labTest2: list nat
labTest2 = filter evenb (O::(S O)::(S (S O))::(S (S (S (S O))))::nil)

sumFold: nat
sumFold = list.foldr add O 
        ((S O)::(S (S O))::(S (S (S O)))::
        S (S (S (S (S (S O)))))::nil) -- 1 + 2 + 3 + 6 =12

productFold: nat
productFold = list.foldr mult (S O) 
            ((S O)::(S (S O))::(S (S (S O)))::
            S (S (S (S (S (S O)))))::nil) -- 1 * 2 * 3 * 6 = 36
