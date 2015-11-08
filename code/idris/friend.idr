module friend

-- Trustworthyness (bool)
-- Name (String)
-- Age (Nat)

import bool

data friend = mkFriend bool String Nat

f1: friend
f1 = mkFriend true "Bud" 100

f2: friend
f2 = mkFriend false "notBud" 666

getAge: friend -> Nat
getAge (mkFriend a b c) = c

