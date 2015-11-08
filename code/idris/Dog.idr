-- How to read:
-- MkDog [Name] [Age in months] [Cuteness qualifier] [Size in cm from
-- paw to head] [Quickness in kph] [Friendliness factor]

module Dog

import bool

record Dog where
      constructor MkDog
      name : String
      age : Nat          --in months
      cute : bool
      size : Nat         --in cm (height)
      quickness : Nat    --in kph
      friendliness : bool
      
AvDog: Dog
AvDog = MkDog "Pup" 12 true 30 30 true

OldDog: Dog
OldDog = MkDog "Oldie" 120 false 50 10 true

BigDog: Dog
BigDog = MkDog "Big Pup" 36 true 80 35 true

FastDog: Dog
FastDog = MkDog "Speedy" 24 true 40 50 true

MeanDog: Dog
MeanDog = MkDog "MeanOne" 6 true 15 20 false
