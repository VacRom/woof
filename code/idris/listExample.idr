module Dogs

import Dog
import list

listDog: list Dog
listDog = AvDog :: OldDog :: BigDog :: FastDog :: MeanDog :: nil

-- Note that we don't need functions for 'name' because we built it in
  -- with 'record Dog where...'
  
-- Example
Name: Dog -> String
Name a = name a

NameTest1: String
NameTest1 = Name AvDog

NameTest2: String
NameTest2 = name AvDog

-- Note that they both return "Pup". So, everything the did in
-- gunrow.idr is already implemented.
