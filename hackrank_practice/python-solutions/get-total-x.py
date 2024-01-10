import math


def getTotalX(a, b):
    count = 0

    lcm_a = a[0]
    for num in a[1:]:
        lcm_a = lcm_a * num // math.gcd(lcm_a, num)

    gcd_b = b[0]
    for num in b[1:]:
        gcd_b = math.gcd(gcd_b, num)

    x = lcm_a
    while x <= gcd_b:
        if gcd_b % x == 0:
            count += 1
        x += lcm_a

    return count
