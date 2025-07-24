import random

def getLotto():
    numbers = []
    while len(numbers) < 6:
        num = random.randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return sorted(numbers)

print("로또 번호:", getLotto())