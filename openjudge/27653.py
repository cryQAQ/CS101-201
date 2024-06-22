from math import gcd
class Fraction:
    def __init__(self,top,bot):
        self.num = top
        self.den = bot
    def __str__(self):
        return str(self.num)+'/'+str(self.den)
    def add(self,fr):
        n_t = self.num * fr.den + self.den * fr.num
        n_b = self.den * fr.den
        g = gcd(n_t,n_b)
        n_t //= g
        n_b //= g
        return Fraction(n_t,n_b)
a,b,c,d = map(int,input().split())
f1,f2 = Fraction(a,b),Fraction(c,d)
print(Fraction.add(f1,f2))