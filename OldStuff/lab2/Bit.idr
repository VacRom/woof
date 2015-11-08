module Bit

-- Data type
data Bit = zero | one

-- Functions
change: Bit -> Bit
change zero = one
change one = zero

id: Bit -> Bit
id zero = zero
id one = one


