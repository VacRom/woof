import bool
import pair
import nat

-- Here are some tests for the fib. seq.
testO: nat
testO = fibp (O)

testS: nat
testS = fibp (S O) 

testSS: nat
testSS = fibp (S (S O))

testSSS: nat
testSSS = fibp (S (S (S O)))

testSSSSSSS: nat
testSSSSSSS = fibp (S (S (S (S (S (S (S O)))))))

-- Returns 0, 1, 1, 2, ... etc 
