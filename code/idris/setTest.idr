module setTest

import set
import nat
import bool
import ite
import eq
import list

s0: set nat
s0 = new_set

s1: set nat
s1 = set_insert (S O) s0

s2: set nat
s2 = set_insert (S O) s1


-- [1,2]
set1: set nat
set1 = mkSet ((S O)::(S (S O))::nil)

-- [2,1]
set2: set nat
set2 = mkSet ((S (S O))::(S O)::nil)
 
-- [3,1]
set3: set nat
set3 = mkSet ((S (S (S O)))::(S O)::nil)

-- [1,3,2]
set4: set nat
set4 = mkSet ((S O)::(S (S (S O)))::(S (S O))::nil)

-- Is set1 contained in set2 AND set2 contained in set1? Expected
  -- answer, true.
test1: bool
test1 = eql_set set1 set2

-- The same but reversed. Still true.
test2: bool
test2 = eql_set set2 set1

-- [1,2] (or [2,1])  is not the same as [1,3]. False.
test3: bool
test3 = eql_set set1 set3

test4: bool
test4 = eql_set set2 set3

-- [1,2] (or any of our other test sets) is the same as [1,3,2]. False
test5: bool
test5 = eql_set set1 set4

test6: bool
test6 = eql_set set4 set1

test7: bool
test7 = eql_set set2 set4

-- etc.. all would be false.

-- A set is always equal to itself. So true.
test8: bool
test8 = eql_set set1 set1

test9: bool
test9 = eql_set set4 set4

