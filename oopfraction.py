class Fraction:

    def __init__(self,x,y):
        self.num = x
        self.den = y
    def __str__(self):
        return '{}/{}'.format(self.num,self.den)
    
    def __add__(self,other):
        temp_num = self.num*other.den+self.den*other.num
        temp_den = self.den*other.den
        return '{}/{}'.format(temp_num,temp_den)
    
obj1 = Fraction(2,3)
obj2 = Fraction(1,4)
print(obj1+obj2)
print(51*42)