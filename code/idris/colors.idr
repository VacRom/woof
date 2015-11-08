module color
import pair
import bool
import comp
%default total

additive: color -> bool
additive red = true
additive green = true
additive blue = true
additive _ = false

subtractive: color -> bool
subtractive x = not (additive x)

complements: pair color color -> bool
complements (mkPair a (comp.complement a)) = true

mixink: pair color color -> color
mixink (mkPair cyan magenta) = blue
mixink (mkPair magenta cyan) = blue
mixink (mkPair magenta yellow) = red
mixink (mkPair yellow magenta) = red
mixink (mkPair yellow cyan) = green
mixink (mkPair cyan yellow) = green
