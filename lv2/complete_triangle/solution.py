from math import gcd

def solution(w,h):
    if gcd(w,h) ==1:
        return (w*h) - (w+h-1)
    else:
        return w*h - (w+h -gcd(w,h))