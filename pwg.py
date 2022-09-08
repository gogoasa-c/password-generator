import random

sym = "[=@-_!#$%^&*()<>?/\|}{~:]"
up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lo = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"

while True:
    password = ""
    lowerC = 0
    upperC = 0
    symbol = 0
    number = 0
    for i in range(16):
        digit = chr(random.randrange(33, 126, 1))
        if str(digit) in up:    
            upperC = 1
        if str(digit) in lo:
            lowerC = 1
        if str(digit) in num:
            number = 1
        if str(digit) in sym:
            symbol = 1
        password+=digit
        
    if upperC == 1 and lowerC == 1 and number == 1 and symbol == 1:
        break

print(password)

