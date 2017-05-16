type_of_chocolate = "dark chocolate"

def food_steps():
    print  "mix all ingredients"
    print "fry"
    print "flip"
    print "plate"

def making_simple_omelette(ingredient):
    food_steps()
    omelette = "I've made a tasty " + ingredient + " omelette"
    print omelette
    return omelette

def making_fancy_omelette(*ingredients):
    food_steps()
    omelette = "I've made a tasty omelette with {} ingredient(s)".format(len(ingredients))
    print omelette
    return omelette

def making_pancake():
    type_of_chocolate = "milk chocolate"
    food_steps()
    pancake = "I've made a delicious {} chip pancake".format(type_of_chocolate)
    print pancake
    return pancake
    print

simple_omelette = making_simple_omelette('cheese')
my_omelette = making_fancy_omelette('cheese', 'tomato', 'basil')
your_omelette = making_fancy_omelette('sausage', 'mushroom', 'bellpepper', 'olives')

my_pancake = making_pancake()
matts_ingredients = ['sausage', 'mushroom', 'bellpepper', 'olives']
matts_omelette = making_fancy_omelette(*matts_ingredients)
