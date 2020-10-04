a = [1, 3, 5, 7, 9]
b = a
b[0] = 5
print(a)

def choose(number, choice=0):
    if choice == 0:
        return choice
    else:
        return number

print(choose(7, 3))