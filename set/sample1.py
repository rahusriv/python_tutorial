#set has no duplicates
#It is unordered

farm_animals = ["sheep", "cow", "hen","goat", "goat"]

farm_animals_set = set(farm_animals)

print(farm_animals_set)

for animal in farm_animals_set:
    print(animal)

farm_animals_set.add("buffalo")

other_animals = ["buffalo","dog","hen","tiger","giraffe", "goat"]

other_animals_set = set(other_animals)

print(farm_animals_set)
print(other_animals_set)

animals_set_union = farm_animals_set.union(other_animals_set)
print(animals_set_union)

animals_set_intersection = farm_animals_set.intersection(other_animals_set)
print(animals_set_intersection)

empty_set = set()
empty_set.add("new element")
empty_list = []
empty_dictionary = {}
empty_tuple = ()
print(farm_animals_set.difference(other_animals_set))

