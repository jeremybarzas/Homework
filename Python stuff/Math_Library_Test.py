import Math_Library
from Math_Library import *

print(" ")
print("======= 2D Vector Maths ======")
print(" ")

Vec2a = Vector2D(6,12)
Vec2b = Vector2D(3,1)

print(" ")
print("2D Vectors to be mathed upon all python like: (6,12) and (3,1)")

print(" ")
print("======= 2D Vector Addition ======")
print(" ")

Vec2sum = Vec2a.add(Vec2b)
Vec2sum.answer()

print(" ")
print("======= 2D Vector Subtraction ======")
print(" ")

Vec2dif = Vec2a.sub(Vec2b)
Vec2dif.answer()

print(" ")
print("======= 2D Vector Multiplication ======")
print(" ")

Vec2product = Vec2a.mul(Vec2b)
Vec2product.answer()

print(" ")
print("======= 2D Vector Division ======")
print(" ")

Vec2quotient = Vec2a.div(Vec2b)
Vec2quotient.answer()

print(" ")
print("======= 2D Vector Magnitude ======")
print(" ")

Vec2mag = Vec2a.mag()
print(Vec2mag)

print(" ")
print("======= 2D Vector Normalization ======")
print(" ")

Vec2norm = Vec2a.norm()
Vec2norm.answer()

print(" ")
print("======= 2D Vector Dot Product ======")
print(" ")

Vec2dotP = Vec2a.dotP(Vec2b)
print(Vec2dotP)

print(" ")
print("======= 2D Linear Interpolation ======")
print(" ")

Vec2lerp = Vec2a.lerp(Vec2b)
Vec2lerp.answer()

print(" ")
print("======= 3D Vector Maths ======")
print(" ")

Vec3a = Vector3D(6,12,4)
Vec3b = Vector3D(3,1,20)

print(" ")
print("3D Vectors to be mathed upon all python like: (6, 12, 4) and (3, 1, 20)")

print(" ")
print("======= 3D Vector Addition ======")
print(" ")

Vec3sum = Vec3a.add(Vec3b)
Vec3sum.answer()

print(" ")
print("======= 3D Vector Subtraction ======")
print(" ")

Vec3dif = Vec3a.sub(Vec3b)
Vec3dif.answer()

print(" ")
print("======= 3D Vector Multiplication ======")
print(" ")

Vec3product = Vec3a.mul(Vec3b)
Vec3product.answer()

print(" ")
print("======= 3D Vector Division ======")
print(" ")

Vec3quotient = Vec3a.div(Vec3b)
Vec3quotient.answer()

print(" ")
print("======= 3D Vector Magnitude ======")
print(" ")

Vec3mag = Vec3a.mag()
print(Vec3mag)

print(" ")
print("======= 3D Vector Normalization ======")
print(" ")

Vec3norm = Vec3a.norm()
Vec3norm.answer()

print(" ")
print("======= 3D Vector Dot Product ======")
print(" ")

Vec3dotP = Vec3a.dotP(Vec3b)
print(Vec3dotP)

print(" ")
print("======= 3D Linear Interpolation ======")
print(" ")

Vec3lerp = Vec3a.lerp(Vec3b)
Vec3lerp.answer()
