# The Collatz Conjecture. this simple script allows you to make "The Collatz Conjecture" calculation in less than a second!
x = int(input("Enter a number:"))
while x != 1:
    print(int(x))
    if (x % 2) == 0:
        x = (x / 2)
    else:
        x = (x * 3) + 1
    if (x == 1):
        break
print(int(x))
