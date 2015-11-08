module ite

import bool

ite: Bool -> a -> a -> a
ite True tb fb = tb
ite _ tb fb = fb

ite': bool -> a -> a -> a
ite' true tb fb = tb
ite' _ tb fb = fb
