# languages = ["Python", "C++", "Java", "Java", "Perl", "Python", "C++", "C#", "Python"]


# # search = "Python"
# search = "python"
# # count = 0
# print(f"Searching for {search}")

# for language in languages:
#     if language == search:
#         print(f"Found {language}")
#         count += 1
#     else:
#         print(f"XXX {language}")

# print("Python" in languages)

# print(f"Thanks for seaching, we found {search} {count} times")

# for language in languages:
#     if language == search:
#         print(f"Found {language}")
#         break
# else:
#     print(f"{search} not found")

# i = 30

# while i >= 0:
#     print(i, end=" ")
#     i -=2
# print()



# initialization = 5
# stop_at = 10
# increment = 1

# for i in range(initialization, stop_at, increment):
#     print("For loop:", i)


# while initialization < stop_at:
#     print("while loop:", initialization)
#     initialization += increment


i = 0
while(i < 5):
    if i**2 > 50:
        print("Square big enough:", i)
        break
    i += 1
else:
    print("None are big enough")




