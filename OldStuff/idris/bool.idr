module bool

data bool = true | false

id: bool -> bool
-- id true = true
-- id false = false
id b = b

constTrue: bool -> bool
-- constTrue true = true
-- constTrue false = true
constTrue _ = true

constFalse: bool -> bool
constFalse _ = false

not: bool -> bool
not true = false
not false = true

