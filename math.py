# task 2
import math
def triangle_type(a, b, c):
    if (a+b>c and a+c>b and b+c>a):
        alpha = round(math.degrees(math.acos((b * b + c * c - a * a) / (2 * b * c))),3)
        betta = round(math.degrees(math.acos((a * a + c * c - b * b) / (2 * a * c))),3)
        gamma = round(math.degrees(math.acos((b * b - c * c + a * a) / (2 * b * a))),3)
        sum=alpha + betta + gamma
        print (sum)
        if round(sum)!=180:
            return 0
        elif (alpha == 90 or betta == 90 or gamma == 90):
            return 2
        elif alpha<90 and betta<90 and gamma<90:
            return 1
        elif (alpha>90 or betta>90 or gamma>90):
            return 3
    else:
        print("k")
        return 0

print(triangle_type(7,12,8))

