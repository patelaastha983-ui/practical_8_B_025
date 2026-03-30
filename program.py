# USER INPUT
symbol = input("Enter symbol: ")
rows = int(input("Enter number of rows: "))

# RIGHT HALF PYRAMID
print("\nRight Half Pyramid:\n")
for i in range(1, rows + 1):
    print((symbol + " ") * i)

# FULL PYRAMID
print("\nFull Pyramid:\n")
for i in range(rows, 0, -1):
    print(" " * (rows - i) + (symbol + " ") * i)

# EVEN NUMBERS
print("\nEven Numbers from 1 to 100:\n")
even_numbers = [i for i in range(1, 101) if i % 2 == 0]

print("List:", even_numbers)
print("Minimum:", min(even_numbers))
print("Maximum:", max(even_numbers))
print("Sum:", sum(even_numbers))