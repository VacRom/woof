import set_adt

import bool
import option
import pair
import list
import nat
import eq
import serialize

import list
import ite

-- {1,2,3}
set1: set nat
set1 = mkSet ((S O)::(S (S O))::(S (S (S O)))::nil)

-- {3,2}
set2: set nat
set2 = mkSet ((S (S (S O)))::(S (S O))::nil)

-- {2,3,4}
set3: set nat
set3 = mkSet ((S (S O))::(S (S (S O)))::(S (S (S (S O))))::nil)

-- Improper set, {1,1,2,3}
set1': set nat
set1' = mkSet ((S O)::(S O)::(S (S O))::(S (S (S O)))::nil)

-- Improper set, {3,2,2}
set2': set nat
set2' = mkSet ((S (S (S O)))::(S (S O))::(S (S O))::nil)

-- {}
test1: set nat
test1 = emptySet {a = nat}

-- {5} u {1,2,3} = {5,1,2,3}
test2: set nat
test2 = set_insert (S (S (S (S (S O))))) set1

-- {5} u {1,1,2,3} = {5,1,2,3}
test3: set nat
test3 = set_insert (S (S (S (S (S O))))) set1'

-- {1} u {1,1,2,3} {5,1,2,3}
test4: set nat
test4 = set_insert (S O) set1'

-- {1,1,2,3} \ {1} = {2,3}
test5: set nat
test5 = set_remove (S O) set1'

-- |{1,1,2,3}| = 3
test6: nat
test6 = set_cardinality set1'

-- |{}| = 0
test7: nat
test7 = set_cardinality (mkSet nil) {a = nat}

-- 2 element of {1,2,3}? True.
test8: bool
test8 = set_member (S (S O)) set1

-- {1,2,3} u {3,2} = {1,2,3}
test9: set nat
test9 = set_union set1 set2

-- {1,2,3} u {2,3,4} = {1,2,3,4}
test10: set nat
test10 = set_union set1 set3

-- {1,2,3} n {2,3,4} = {2,3}
test11: set nat
test11 = set_intersection set1 set3

-- {1,2,3} n {} = {}
test12: set nat
test12 = set_intersection set1 emptySet {a = nat}

-- {1,2,3} \ {2,3,4} = {1}
test13: set nat
test13 = set_difference set1 set3

-- {1,1,2,3} \ {1,2,3} = {}
test14: set nat
test14 = set_difference set1' set1

-- Is {1,2,3} all even? False.
test15: bool
test15 = set_forall evenb set1

-- Is {} all even? True.
test16: bool
test16 = set_forall evenb emptySet {a = nat}

-- E even {1,2,3}? True.
test17: bool
test17 = set_exists evenb set1

-- E even {}? False. Notice that even though {} is all even we can't
  -- find a single even value.
test18: bool
test18 = set_exists evenb emptySet {a = nat}

-- Provides an example of an even number from {1,2,3}. E.g. Some 2.
test19: option nat
test19 = set_witness evenb set1

-- Gives all cross products of {1,2,3} and {3,2} = {(1,3),(1,2),...}
test20: set (pair nat nat)
test20 = set_product set1 set2

-- Note that this function hasn't been refined with the checker
  -- function, so there are some duplicate answers.
test21: set (pair nat nat)
test21 = set_product set1' set2

-- Are the sets equal? Reflexive law says yes.
test22: bool
test22 = eql set1 set1

-- {1,2,3}={1,1,2,3}
test23: bool
test23 = eql set1' set1

-- {1,2,3}=/={2,3,4}
test24: bool
test24 = eql set1 set3

-- {1,2,3} = "{sZ,ssZ,sssZ}"
test25: String
test25 = toString set1

-- {1,2,3} = "{sZ,ssZ,sssZ}"
test26: String
test26 = toString set1'
