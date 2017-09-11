#! env bin/python
# codding = utf-8
import turtle
import pprint
import math


def calculating(a1, b1, c1):
    if a1 + b1 > c1 and b1 + c1 > a1 and a1 + c1 > b1:
        return True
    else:
        return False


def calculating_angles(a, b, c):
    alpha = (math.pow(a, 2) + math.pow(b, 2) - math.pow(c, 2)) / (2 * a * b)
    alpha_a = math.acos(alpha)
    alpha_degrees = math.degrees(alpha_a)
    print(alpha_degrees)

    beta = (math.pow(c, 2) + math.pow(b, 2) - math.pow(a, 2)) / (2 * c * b)
    beta_a = math.acos(beta)
    beta_degrees = math.degrees(beta_a)
    print(beta_degrees)

    gamma = (math.pow(a, 2) + math.pow(c, 2) - math.pow(b, 2)) / (2 * c * a)
    gamma_a = math.acos(gamma)
    gamma_degrees = math.degrees(gamma_a)
    print(gamma_degrees)
    return alpha_degrees, beta_degrees, gamma_degrees


def triangle(turtle1, x, y, a, b, c):
    alpha, beta, gamma = calculating_angles(a, b, c)
    turtle1.pu()
    turtle1.setpos(x, y)
    turtle1.pd()
    turtle1.forward(a)
    turtle1.left(180-alpha)
    turtle1.forward(b)
    turtle1.left(180-beta)
    turtle1.forward(c)
    input()


print("Input a ")
A = int(input())
print("Input b ")
B = int(input())
print("Input c ")
C = int(input())
print('Input coordinates first point x1 = ')
x1 = int(input())
print('Input coordinates first point y1 = ')
y1 = int(input())

info = calculating(A, B, C)

if info:
    calculating_angles(A, B, C)
    test = turtle.Turtle()
    pprint.pprint(dir(test))
    triangle(test, x1, y1, A, B, C)
else:
    print("Input correct data")

