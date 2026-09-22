num = int(input("Enter a 3-digit positive integer: "))
print("Decimal:", num)
print("Binary:", bin(num))
print("Octal:", oct(num))
print("Hexadecimal:", hex(num))
print("Last digit:", num % 10)
if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")