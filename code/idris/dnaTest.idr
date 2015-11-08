module dnaTest

import dna
import list
import pair

test1: base
test1 = complement_base A -- T

test2: base
test2 = complement_base T -- A

test3: base
test3 = complement_base C -- G

test4: base
test4 = complement_base G -- C

testStrand1: list base
testStrand1 = (A::T::C::G::A::A::A::A::nil)

testStrand2: list base
testStrand2 = (T::A::G::C::T::T::T::T::nil) -- complement of the above

testPair1: list (pair base base)
testPair1 = ((mkPair A T)::(mkPair T A)::(mkPair C G)::(mkPair G C)::nil)

testPair2: list (pair base base)
testPair2 = ((mkPair T A)::(mkPair A T)::(mkPair G C)::(mkPair C G)::nil)

testPairStrand1: list base
testPairStrand1 = strand1 testPair1 -- [A,T,C,G]

testPairStrand2: list base
testPairStrand2 = strand2 testPair1 -- [T,A,G,C]

testComplete1: list (pair base base)
testComplete1 = complete testStrand1 -- [AT,TA,CG,GC,AT,AT,AT,AT]

testComplete2: list (pair base base)
testComplete2 = complete testStrand2 -- [TA,AT,GC,CG,TA,TA,TA,TA]

testCount: Nat
testCount = countBase A testStrand1 --5
