# Asks for the length and width of 2 rectangles, then displays the areas
# 9/17/19
# CTI-110 P3T1 - Areas Of Rectangles
# Dennis Walker
#

""" Pseudocode """
# Ask the user for the length and width of rectangle A
# Ask the user for the length and width of rectangle B
# Calculate the Area of rectangles A and B
# Determine which rectangle has the larger area
# Display the area of rectangle A and B, seperately
# Display a message to the user - which area is larger
# End program

print("This program find the area of 2 rectangles, then it compares them.\n")

# Requests info for square A
len_A = float(input("Input the length of rectangle A: "))
wid_A = float(input("Input the width of rectangle A: "))
if len_A == wid_A:
    print("\tThats a square silly, but I can process it anyway")

# Requests info for square B
len_B = float(input("\nInput the length of rectangle B: "))
wid_B = float(input("Input the length of rectangle B: "))
if len_B == wid_B:
    print("\tThats a square silly, but I can process it anyway")

# Calculates the areas of each square
area_A = len_A * wid_A
area_B = len_B * wid_B

# Prints the areas of each square
print(f"\nThe area of rectangle A is {area_A}")
print(f"The area of rectangle B is {area_B}")

# Determines which area is larger, or if they are the same
if area_A > area_B:
    print(f"\nThe area of Rectangle A ({int(area_A)}) is larger than the area of rectangle B ({int(area_B)}) ")
elif area_A < area_B:
    print(f"\nThe area of Rectangle B ({int(area_B)}) is larger than the area of rectangle A ({int(area_A)}) ")
elif area_A == area_B:
    print(f"\nThe area of Rectangle A ({int(area_A)}) and Rectangle B ({int(area_B)}) are the same!")
