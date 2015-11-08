module burrito

import list

data burrito = Chicken | Steak | Barbacoa | Carnitas | Sofritas

data burritorow = mkBurrito burrito Nat Nat Nat Nat

||| mkBurrito [Type of protein] [Calories] [Fat (grams)] [Carbs (grams)] [Protein (grams)]

chicken: burritorow
chicken = mkBurrito Chicken 190 7 1 32

steak: burritorow
steak = mkBurrito Steak 190 7 2 30

barbacoa: burritorow
barbacoa = mkBurrito Barbacoa 170 7 2 24

carnitas: burritorow
carnitas = mkBurrito Carnitas 190 8 1 27

sofritas: burritorow
sofritas = mkBurrito Sofritas 145 10 9 8

listBurrito: list burritorow
listBurrito = chicken :: steak :: barbacoa :: carnitas :: sofritas :: nil
