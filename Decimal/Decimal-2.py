from decimal import Decimal

#tuple_num = (0, (8, 7, 4), -6) #0.000874
tuple_num = (1, (1, 2, 3), 4)  #-1230000 типа Decimal
decimal_num = Decimal(tuple_num)
print(decimal_num, "\n")

print(Decimal((0, (3, 1, 4), -1)))
print(Decimal((1, (3, 1, 4), 0)))
print(Decimal((0, (3, 1, 4), 1)))
print(Decimal([1, (3, 1, 4), 2]))

num_constructor = [1, (5, 2, 7), 0]
num_decimal = Decimal(num_constructor)
print(num_decimal)


print("\n")
print('+'*15)

print(1.4, round(1.4))
print(1.5, round(1.5))
print(1.7, round(1.7))

print(2.3, round(2.3))
print(2.5, round(2.5))
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