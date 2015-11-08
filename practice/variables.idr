-- Multiplication table for Z5

module unit

data unit = one | two | three | four | five

MOne: unit -> unit
MOne b = b

MTwo: unit -> unit
MTwo One = two
MTwo two = four
MTwo three = One
MTwo four = three
MTwo five = five

MThree: unit -> unit
MThree One = three
MThree two = One
MThree three = four
MThree four = Two
Mthree Five = Five
