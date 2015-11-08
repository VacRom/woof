module bool

import serialize

data bool = true | false

id: bool -> bool
id b = b

constFalse: bool -> bool
constFalse _ = false

constTrue: bool -> bool
constTrue _ = true

not: bool -> bool
not true = false
not _ = true

and: bool -> bool -> bool
and true true = true
and _ _ = false

or: bool -> bool -> bool
or true _ = true
or false n = n

xor: bool -> bool -> bool
xor true n = not n
xor false n = n

nand: bool -> bool -> bool
nand true n = not n
nand false _ = true

eql_bool: bool -> bool -> bool
eql_bool true true = true
eql_bool false false = true
eql_bool _ _ = false

instance serialize bool where
  toString true = "True"
  toString false = "False"
