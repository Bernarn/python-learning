# Tuples are like list but instead [] they use ()
# Tuples are immutable , that's mean you can't change it's elements once it created 

fruits=("mango", "apple", "pineapple", "guava")
print(len(fruits))
# Tuples can contain mixed data types and even nested structures

colors=("Blue", "Yellow", "Green", ["Green families"])
print(colors)
# Even though the tuple itself can’t be changed, the list inside it can be modified:
colors[3].append("green Vert")
print(colors)
# Unpacking a tuple
person=("Bernard", 22, "Benin")
name, age, country=person

print(f"your name is {name} , you are {age} years old , and your country is {country}. /n Nice to meet {name}")

# if the number of variables doesn’t match the number of items in the tuple,
# 👉 Python will raise an error (ValueError) because it doesn’t know how to assign the extra or missing values.
# To handle that we will make use  :
# You can use * to “catch” extra values. The * (star) in unpacking collects extra values into a list.

name, *countryAge=person
print(f"Your details are {name}, {countryAge}")
