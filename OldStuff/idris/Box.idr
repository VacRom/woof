module Box
import bool

data Box = mkbox bool

b1: Box
b1 = mkbox true

b2: Box
b2 = mkbox false

unbox: Box -> bool
unbox (mkbox b) = b
