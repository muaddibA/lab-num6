num = int(input('Ваши циферки: '))
def rot(num):
    num = str(num)
    num = num.replace('6', '9', 1)
    return int(num)
print(rot(num))