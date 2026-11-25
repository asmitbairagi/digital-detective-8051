num = int(input("Enter a decimal number: "))
binary = bin(num)
octal = oct(num)
hexa = hex(num)

print("Binary:", binary)
print("Octal:", octal)
print("Hexadecimal:", hexa)

binary_input = input("Enter a binary number: ")
octal_input = input("Enter an octal number: ")
hex_input = input("Enter a hexadecimal number: ")

print("Binary to decimal:", int(binary_input, 2))
print("Octal to decimal:", int(octal_input, 8))
print("Hexadecimal to decimal:", int(hex_input, 16))