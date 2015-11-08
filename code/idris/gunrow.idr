module gunrow

import list

data country = Argentina | Austrialia | Austria | Hounduras | USA

||| A record of this type represents a country and the death rate per 10,000,000 by gun for: Homicides, Suicides, Unintentional, and Undetermined deaths.

data gunrow = mkGunrow country Nat Nat Nat Nat

argentina: gunrow
argentina = mkGunrow Argentina 190 279 64 362

austrailia: gunrow
austrailia = mkGunrow Austrialia 11 62 5 8

austria: gunrow
austria = mkGunrow Austria 18 268 1 8

hounduras: gunrow
hounduras = mkGunrow Hounduras 648 0 0 0

usa: gunrow
usa = mkGunrow USA 355 670 16 9

name: gunrow -> country
name (mkGunrow a b c d e) = a

homicides: gunrow -> Nat
homicides (mkGunrow a b c d e) = b

suicides: gunrow -> Nat
suicides (mkGunrow a b c d e) = c

unintentional: gunrow -> Nat
unintentional (mkGunrow a b c d e) = d

undetermined: gunrow -> Nat
undetermined (mkGunrow a b c d e) = e

totaldeaths: gunrow -> Nat
totaldeaths (mkGunrow a b c d e) = b+c+d+e

listGunrow: list gunrow
listGunrow = cons argentina (cons austrailia (cons austria (cons hounduras (cons usa nil))))
