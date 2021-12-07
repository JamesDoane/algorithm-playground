#ROT13 conversion algorithm. 5 kyu. O(n)
def rot13(message):
    new_message = []
    for x in message:
        if x.isalpha():
            if ord(x) > 96 and ord(x) < 110:
                y = ord(x) + 13
            elif ord(x) > 109:
                y = ord(x) - 13
            elif ord(x) > 64 and ord(x) < 78:
                y = ord(x) + 13
            else:
                y = ord(x) - 13
        
            new_message.append(chr(y))
        else:
            new_message.append(x)
    
    result = ''.join(new_message)
        
    return result

#Twice Linear. 4kyu. O(n)
def dbl_linear(n):
    u = [1]
    ai = 0
    bi = 0
    while len(u) < n+1:
        y = (2 *u[ai]+1)
        z = (3 *u[bi]+1)
        if y < z:
            u.append(y)
            ai += 1
        elif z<y:
            u.append(z)
            bi += 1
        else:
            u.append(y)
            ai += 1
            bi += 1
    return u[n]

#Score dice game of 5 die. 5 kyu. O(n)
def score(dice):
    ones = []
    twos = []
    threes = []
    fours = []
    fives = []
    sixes = []
    score = 0
    for die in dice:
        if die == 1:
            ones.append(die)
        if die == 2:
            twos.append(die)
        if die == 3:
            threes.append(die)
        if die == 4:
            fours.append(die)
        if die == 5:
            fives.append(die)
        if die == 6:
            sixes.append(die)
    
    if len(ones) >= 3:
        score += 1000 + ((len(ones)-3)*100)
    else:
        score += 100 * len(ones)
    if len(twos) >= 3:
        score += 200
    if len(threes) >= 3:
        score += 300
    if len(fours) >= 3:
        score += 400
    if len(fives) >= 3:
        score += 500 + ((len(fives)-3)*50)
    else:
        score += 50 * len(fives)
    if len(sixes) >= 3:
        score += 600
    
    return score

#Validate ISBN-10 numbers. 5 kyu. O(n)
def valid_ISBN10(isbn):
    if len(isbn) != 10:
        return False
    sum = 0
    for i, x in enumerate(isbn):
        if x == 'X' and i == 9:
            sum += 10 * (i+1)
        elif x.isalpha():
            return False
        else:
            sum += int(x) * (i+1)
    if sum % 11 == 0:
        return True
    
    return False

#Mean Square. 5 kyu. O(n)
def solution(array_a, array_b):
    average = 0
    for i, x in enumerate(array_a):
        difference = abs(x - array_b[i])
        average += difference ** 2
    
    average = average/len(array_a)
    return average

#Beearmid (how many beers can be made into a pyramid given a bonus and price of beer). 5 kyu. O(n)
def beeramid(bonus, price):
    number_of_beers = bonus/price
    layer = 0
    while number_of_beers > 0:
        number_of_beers -= layer ** 2
        if number_of_beers == 0:
            return layer
        if number_of_beers < 0:
            return layer - 1
        layer += 1
    
    return layer