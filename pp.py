def isPP(n):
    for i in range(n):
        for j in range(n):
            if j**i == n:
                return [i,j]
    return None


print(isPP(99))
print(isPP(81))
print(isPP(77))
print(isPP(144))
print(isPP(996))
print(isPP(3453467))
print(isPP(34534))
print(isPP(378678678))