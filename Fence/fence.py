# 
import random
import time

LEN = 188

k = 11
num = int(LEN/k)+1 if LEN%k != 0 else int(LEN/k)

while True:
    line = ''
    for i in range(num):
        x = random.randint(32,255)
        while x == 127 or x == 160 or x == 173 or x in range(128,160):
            x = random.randint(32,255)
        
        line += str(chr(x))

    line = (' '*(k-1)).join(line)
    
    print(line, end='\n')
    print()
    
    time.sleep(0.05)
    
    
'''GPT

import random
import time

LEN = 188
k = 11

num = (LEN + k - 1) // k

def generate_random_char():
    while True:
        x = random.randint(32, 255)
        if x not in {127, 160, 173} and not (128 <= x < 160):
            return chr(x)

while True:
    line = ''.join(generate_random_char() for _ in range(num))
    formatted_line = (' ' * (k - 1)).join(line)
    
    print(formatted_line)
    time.sleep(0.05)

'''