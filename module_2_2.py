first = 76
second = 76
third = 76
if first == second == third:
    print('3')
elif first == (first == second) or (second == third) or (first == third):
    print('2')
else:
    print('0')