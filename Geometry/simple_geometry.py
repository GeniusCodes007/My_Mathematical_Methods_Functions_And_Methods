import math

#gives the whole part of the quotient of num1 and num2, where num2 divides num1
def mod_whole(base_num, divisor):
    return float(base_num) // float(divisor)

#print(mod_whole(1, 2))

#gives the remainder of the quotient of num1 and num2, where num2 divides num1.
def mod_rem(base_num, divisor):
    return float(base_num) % float(divisor)



#gives the remainder of the quotient of num1 and num2 as a fraction of num2, while num2 divides num1
def mod_frac_rem(base_num, divisor):
    return str(int(mod_rem(base_num, divisor))) + "/" + str(divisor)




def sine2(base_num, angle):
    if mod_rem(angle, 360) == 30:
        return base_num * 1/2
    elif mod_rem(angle, 360) == 0:
        return 0.0
    elif mod_rem(angle, 360) == 90:
        return 1.0
    elif mod_rem(angle, 360) == 180:
        return base_num * 0.0
    elif mod_rem(angle, 360) == 270:
        return base_num * -1.0
    else:
        sin = math.sin(math.pi*(angle/180))
        return float(base_num * sin)



def cos2(base_num, angle):
    if mod_rem(angle, 360) == 0:
        return 1.0 * base_num
    elif mod_rem(angle, 360) == 90:
        return 0.0 * base_num
    elif mod_rem(angle, 360) == 180:
        return -1.0 * base_num
    elif mod_rem(angle, 360) == 270:
        return 0.0 * base_num
    else:
        cos = math.cos(math.pi*(angle/180))
        return float(base_num * cos)




def tan2(base_num, angle):
    try:
        s = sine2(base_num, angle)
        c = cos2(base_num, angle)
        tan = s/c
        return tan * base_num
    except ZeroDivisionError:
        return "For " + str(angle) + " The Result Is Undefined" + "\nDivision By Zero Is Infinite"



def square(base_num):
    return float(base_num) ** float(2)


def square_root(base_num):
    return float(base_num) ** float(0.5)



def circumference(r):
    result = (2 * 22 * r) / 7
    return str(result)
print(circumference(7))

def area(r):
    result = (22/7)*(r ** 2)
    return result

print(area(7))


def finding_c(a, b):
    result = square_root(float(square(a))+float(square(b)))
    return result


def finding_a(c, b):
    result = square_root(float(square(c))-float(square(b)))
    if c <= b:
        return "Not Possible !!!"
    else:
        return result


def finding_b(c, a):
    result1 = square_root(float(square(c))-float(square(a)))
    if c <= a:
        return "Not Possible !!!"
    else:
        return result1


def pythatriple():
    what = input("Find What: ")
    if what == "C" or "c":
        num1 = float(input("Give A Number: "))
        num2 = float(input("Give Another Number: "))
        result1 = finding_c(num1, num2)
        return result1
    elif what == "A" or "a":
        num1 = float(input("Give A Number: "))
        num2 = float(input("Give Another Number: "))
        result2 = finding_a(num1, num2)
        return result2
    elif what == "B" or "b":
        num1 = float(input("Give A Number: "))
        num2 = float(input("Give Another Number: "))
        result3 = finding_b(num1, num2)
        return result3
    else:
        inference = "CHECK YOUR VALUES"
        return inference


print(finding_a(7, 4))
print(finding_c(5.744562646538029, 4))
print(__name__)
print(pythatriple())