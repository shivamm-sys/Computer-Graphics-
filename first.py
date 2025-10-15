import math

# Define 2D point 
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

#Translation 
tx = float(input("Enter translation factor tx: "))
ty = float(input("Enter translation factor ty: "))
x_translated = x + tx
y_translated = y + ty
print("\nAfter Translation: (", x_translated, ",", y_translated, ")")

#Scaling
sx = float(input("\nEnter scaling factor sx: "))
sy = float(input("Enter scaling factor sy: "))
x_scaled = x * sx
y_scaled = y * sy
print("After Scaling: (", x_scaled, ",", y_scaled, ")")

#Rotation
angle = float(input("\nEnter rotation angle in degrees: "))
radian = math.radians(angle)
x_rotated = x * math.cos(radian) - y * math.sin(radian)
y_rotated = x * math.sin(radian) + y * math.cos(radian)
print("After Rotation: (", round(x_rotated, 2), ",", round(y_rotated, 2), ")")