import random, string

lung = input("Password semplice: s | Password complicata: c --> ")

if(lung == 'c'):
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(20))
else:
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))

print("\n")
print(x)