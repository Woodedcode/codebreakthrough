# name = input("Hello, what is your name? ")
# print(f"Welcome {name}, have a great day!")

num1, num2 = input("2 favorite numbers (for example: 5 10 ): ").split()
# num2 = float(input("Number 2: "))

print(type(num1), type(num2))

print(f"{num1} + {num2} = {float(num1) + float(num2)}")
