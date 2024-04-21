import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or min >= max or quantity > (max - min + 1):
     return []
    numbers = random.sample(range(min, max + 1),quantity)
    numbers.sort()
    return numbers

lottery = get_numbers_ticket(1, 1000, 4)
print(lottery)