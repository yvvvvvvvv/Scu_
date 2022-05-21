import random
class lottery():
    def lotto():
        a = []
        while len(a)<6:
            b = random.randint(1,49)
            if b not in a:
                a.append(b)
        return a

b = lottery.lotto()
print(b)