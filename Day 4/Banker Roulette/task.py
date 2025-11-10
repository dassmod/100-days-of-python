import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_integer = random.randint(0,4)
name = friends[random_integer]
print(f"{name} will pay the bill.")