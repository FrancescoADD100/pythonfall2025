

def calculate_area(length, width):
    return length * width

def calculate_area_circle(radius):
    return 3.14159 * radius * radius

def calculate_area(base, height):
    return 0.5 * base * height

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
print(f"Area of the rectangle: {calculate_area(length, width):.2f}")

radius = int(input("Enter the radius of the circle: "))
print(f"Area of the circle: {calculate_area_circle(radius):.2f}")

base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
print(f"Area of the triangle: {calculate_area(base, height):.2f}")