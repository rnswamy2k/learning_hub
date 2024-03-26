import math

def number_is_prime(num:int)->bool:
    for i in range(2,num):
        if num%i==0:
            return False
    return True