import random

Str_A = random.randint(1, 255)
Str_B = random.randint(1, 255)
Str_C = random.randint(1, 255)
Str_D = random.randint(1, 255)
RandomIPv4 = '%d.%d.%d.%d' % (Str_A, Str_B, Str_C, Str_D)
print(RandomIPv4)
