# A set is a collection of unique and unordered items.

# Unique → No duplicates allowed.

# Unordered → Items don’t have a fixed position, so you can’t access them by index.
countries={"Benin", "Nigeria", "Kenya", "kenya", "Nigeria"}
print(countries)
# adding to a list
countries.add("Liberia")
#Removing an item: return error if item does not exits
countries.remove("kenya")
# Remove an item safely using the .discard(item)
countries.discard("Liberia")
# length of a set 

len(countries)

# check if am element belong to 
print("Benin" in countries)

# Set Operations(  union |, intersection &, symetric difference ^, difference -,)
flags={"Benin", "Nigeria", "Malawi", "Cameroon", "Niger"}

uni=countries | flags
intersec=countries & flags
symetdiff=countries^flags
