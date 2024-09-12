# import math

# def herons_formula(a, b, c):
#     s = (a + b + c) / 2
#     area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#     return area

# def basic_area(base, height):
#     return 0.5 * base * height

# def trigonometric_area(a, b, angle_C_degrees):
#     angle_C_radians = math.radians(angle_C_degrees)
#     return 0.5 * a * b * math.sin(angle_C_radians)

# def pythagorean_theorem(a, b):
#     return math.sqrt(a**2 + b**2)

# def law_of_sines(a, A_degrees, b, B_degrees):
#     A_radians = math.radians(A_degrees)
#     B_radians = math.radians(B_degrees)
#     return a / math.sin(A_radians) == b / math.sin(B_radians)

# def law_of_cosines(a, b, angle_C_degrees):
#     angle_C_radians = math.radians(angle_C_degrees)
#     c_squared = a**2 + b**2 - 2 * a * b * math.cos(angle_C_radians)
#     return math.sqrt(c_squared)

# # Example usage:

# # Heron's Formula
# a = 5
# b = 6
# c = 7
# print("Area using Heron's formula:", herons_formula(a, b, c))

# # Basic Area Formula
# base = 5
# height = 6
# print("Area using base and height:", basic_area(base, height))

# # Trigonometric Formula
# a = 5
# b = 6
# angle_C = 90  # Angle in degrees
# print("Area using trigonometric formula:", trigonometric_area(a, b, angle_C))

# # Pythagorean Theorem
# a = 3
# b = 4
# print("Hypotenuse using Pythagorean theorem:", pythagorean_theorem(a, b))

# # Law of Sines
# a = 5
# A = 30
# b = 6
# B = 45
# print("Law of Sines check:", law_of_sines(a, A, b, B))

# # Law of Cosines
# a = 5
# b = 6
# angle_C = 60  # Angle in degrees
# print("Third side using Law of Cosines:", law_of_cosines(a, b, angle_C))





#method 1
# b=5
# h=6
# w=7


# area=.5*b*h
# print("Area using base and height:", area)

#method 2

# import math

# # Given sides of the triangle
# a = 5
# b = 6
# c = 7

# # Heron's formula
# s = (a + b + c) / 2
# area_heron = math.sqrt(s * (s - a) * (s - b) * (s - c))
# print("Area using Heron's formula:", area_heron)


