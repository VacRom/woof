module relationTest

import relation
import Person
import People
import bool
import list
import pair
import Dog
import listExample
import ite

queryTest: Nat
queryTest = relation.query people trustworthy age plus 0

-- This takes the RELATION people, SELECTS the trustworthy ones, PROJECTS
  -- their ages, and then REDUCES the list by addition to a single natrual number. Expected value is 41.

countTest: Nat
countTest = count_rel people trustworthy

-- This takes the RELATION people, SELECTS the trustworthy ones,
-- PROJECTS 1 for each trustworthy member, and REDUCES the list by
-- addition to a single natural number. Expected value is 2.

sumTest: Nat
sumTest = sum_rel people trustworthy strength

-- This takes the RELATION people, SELECTS the trustworthy ones,
-- PROJECTS their strength value, and REDUCES the list by addition to
-- a single natural number. Expected value is 8.

aveChar: pair Nat Nat
aveChar = mkPair 
           (query people trustworthy charisma plus 0) 
           (query people trustworthy countOne plus 0)
           
-- This takes the RELATION people, SELECTS the trustworthy ones,
-- PROJECTS their charisma value, and REDUCES the list by addition to
-- a single natural number.
-- The second value in the pair is the same except that it REDUCES the
-- list by adding one for each element in the list.
-- Expected value (mkPair 8 2)
-- This in turn gives us the AVERAGE charisma value for the members of
-- our trustworthy people.

-- Now we take Dog.idr which has a list of dogs (not people) and their
-- attributes. We can calculate many things with our new
-- functions. For example, what is the average age of our CUTE (bool) dogs?

dogTest1: pair Nat Nat
dogTest1 = mkPair
           (query listDog cute age plus 0) 
           (query listDog cute countOne plus 0)

-- This takes the RELATION dog, SELECTS the cute ones, PROJECTS their
-- age values, and REDUCES the list by addition to a single natural
-- number. (For the numerator. The denominator was already discussed
-- in an example above).
-- Expected value (mkPair 78 4)

-- Let's try something new. Define a function that takes a list nat and
-- produces a Nat that is the largest Nat in that list.

head: list Nat -> Nat
head nil = 0
head (h::t) = h

max'': list Nat -> Nat
max'' nil = 0
max'' (a::b::nil) = head (ite (Nat.gte a b) (a::nil) (b::nil))

max': list Nat -> list Nat
max' nil = nil
max' (h::h'::t) = ite (Nat.gte h h') (h::(max' t)) (h'::(max' t))

max: list Nat -> Nat
max nil = 0
max (h::t) = max'' (max' (h::t))

-- So max takes a list and returns the max value of the list. In the
-- case of the empty list it returns 0. We can't change this until we
-- use option.

-- Now let's make a test that takes a RELATION listDog, SELECTS cute,
-- PROJECTS quickness, and REDUCES max.

dogTest2: Nat
dogTest2 = relation.query listDog cute quickness max 0

-- Expected value 50.
-- So this takes listDog, chooses the cute ones, chooses the quickness
-- values, chooses the maximum value from this selection with the
-- identity element being 0. And indeed, the quickest cute dog from
-- our list of dogs has a speed of 50.

