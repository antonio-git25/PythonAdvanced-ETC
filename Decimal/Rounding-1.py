from math import ceil
from math import floor


print("\n")
print('+'*15)

print(1.4, round(1.4))
print(1.7, round(1.7))

print(2.3, round(2.3))
print(2.8, round(2.8))

print(3.5, round(3.5))
print(4.5, round(4.5))

print(-1.5, round(-1.5))
print(-2.5, round(-2.5))
print(-3.5, round(-3.5))
print(-4.5, round(-4.5))



print("\n")
print('P' * 25)
num = 365.345
print(round(num, -2)) # округление до сотен
print(round(num, -1)) # округление до десятков
print(round(num)) # округление до единиц
print(round(num, 1)) # округление до десятых
print(round(num, 2)) # округление до сотых
print(round(num, 3)) # округление до тысячных



print("\n")
print('R' * 25)
print(ceil(4.2))
print(ceil(2.8))
print(ceil(-3.9))
print(ceil(-2.1))
print(ceil(2))
print(ceil(-3))


print("\n")
print('Q' * 25)
print(floor(4.2))
print(floor(2.8))
print(floor(-3.9))
print(floor(-2.1))
print(floor(2))
print(floor(-3))


def capital_bank():
    pass