# data = "hello123"
# character = 'c'
# print(data)
# print(character)
# character = '"here is a message in quotes"'
# print(character)

# data = 'they\'re'
# print(data)
# data = 'they\tre'
# print(data)
# data = 'they\nre'
# print(data)
# data = '\\n is a newline'
# print(data)
# # raw string
# data = r'\\n is a newline'
# print(data)
# data = r'\\n \' \t is a newline ' + '\\'
# print(data)
# data = 'me' + ' + ' + 'you'
# print(data)
# print("me", "+", "you")


# me = "Ryan"
# you = "Caleb"

# print(me, "+", you)
# # string interpolation
# data = f"{me} + {you} are bestest of friends."
# print(data)
# # multiline strings
# data = f"""{me} + {you} are bestest of friends. \
# We met in 3rd grade
# """
# print(data)



message = "This is a very important message."
print(message[0])
print(message[0] + "acos")
print(message[0:3])

# string immutability
msg = "Java is my favorite"
# msg[0] = 'k'
print(msg)
new = "K" + msg[1:]
print(new)

language = "Java"
language += " is actually coffee"
print(language)


# length of strings
name = "Ryan"
print(len(name))
print("Index 2:", name[2])
print("Last index:", name[len(name) - 1])


print("length is", len(name))

message = "length is" + str(len(name))
