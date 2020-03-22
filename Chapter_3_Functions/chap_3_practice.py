def collatz(number): 
    if number % 2 == 0:
        c = number/2
        print(f"{number} / 2 = {int(c)}")
        return int(c)
    else:
        c = 3 * number + 1
        print(f"3 * {number} + 1 = {c}")
        return c

try:
    number = int(input("Give me a number: "))
except ValueError:
    number = int(input("That's not an integes. Please enter an integer:"))

while number != 1:
    number = collatz(number)
else:
    print("U got the 1.")