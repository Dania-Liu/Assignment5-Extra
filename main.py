import math

# Shows the title.
print("Calculating the Area and Circumference of a Circle!")
# Sets variables to default.
firstDiameter = 0
secondDiameter = 0
firstResult = 0
secondResult = 0

# Makes  calculations for area using user input.
firstDiameter = input("Enter diameter to determine area: ")
firstResult = float(math.pi) * ((float(firstDiameter) / 2) * (float(firstDiameter) / 2))
# Displays answer.
print("The area of your circle is:")
print(firstResult)
# Makes  calculations for circumference using user input.
secondDiameter = input("Enter diameter to determine circumference: ")
secondResult = 2 * float(math.pi) * (float(secondDiameter) / 2)
# Displays answer.
print("The circumference of your circle is:")
print(secondResult)
