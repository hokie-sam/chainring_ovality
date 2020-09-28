
import math

ovality = float(input('Ovality (decimal): '))
perimeter = float(input('Teeth: '))

left = 2 * ( (perimeter / (2 * math.pi)) ** 2)
right = 2 - 2 * ovality + ovality**2

a = math.sqrt(left/right)
b = a - ovality*a

round_radius = perimeter/math.pi/2

print(f"\nLongest radius (a) is {round(a,2)}")
print(f"This feels like using a {round(a*2*math.pi,1)} tooth chainring\n")
print(f"Shortest radius (b) is {round(b,2)}")
print(f"This feels like using a {round(b*2*math.pi,1)} tooth chainring\n")
print(f"A circular chainring with {int(perimeter)} teeth would have a radius of {round(round_radius,2)}")
input()
