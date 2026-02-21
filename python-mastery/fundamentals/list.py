# arrays
# static array - python does not have
#amortized


# import copy

# ages = [12,14,16,18,209]
# names = ["Ryan", "Annie", "Olive"]
# mix = ["Ryan", 36, ["Annie", "Olive"]]
# my_favorite_things = ["working out",7,["Netflix", "Amazon Prime"]]
# my_favorite_things[2][1] = "Hulu"

# # DEEP COPY
# print("Before")
# other = copy.deepcopy(my_favorite_things)

# # SHALLOW COPY
# other = my_favorite_things[:]
# other[0] = "Coding"
# other[2][1] = "Disney Plus"





# print(ages)
# print(names)
# print(mix)
# print(my_favorite_things[2][1])
# print(my_favorite_things)
# print(other)



good = ["Kale", "Broccoli", "Spinach"]
bad = ["Pizza", "Fries", "Wings"]

# good += bad
# print(good)


# METHOD
good.extend(bad)
print(good)

# POP
removed = good.pop(0)
print(removed,good)

# APPEND
good.append("Mac and Cheese")
print(good)













