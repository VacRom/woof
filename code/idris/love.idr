module loves

import pair

data person = mary | maurice

loves: person -> person
loves mary = maurice
loves maurice = maurice

p1: pair person person
p1 = mkPair mary maurice

p2: pair person person
p2 = mkPair maurice maurice
