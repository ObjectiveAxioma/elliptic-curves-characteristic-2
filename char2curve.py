class Curve():
    
    # Input: (a1=0? 0/1, first constant (c1), second constant (c2), c3 if a1 = 0)
    def __init__(self, t=0, c1=0, c2=0, c3=0):
        self.c1 = c1
        self.c2 = c2
        self.t = t
        if self.t == 1:
            self.c3 = c3

    def buildCurve(self):
        self.t = int(input("a = 0? (0/1): "))
        if self.t == 0:
            print("Equation is of the form: y^2 + xy = x^3 + ax^2 + b")
        else:
            print("Equation is of the form: y^2 + ay = x^3 + bx + c")
        self.c1 = int(input("Value for a: "))
        self.c2 = int(input("Value for b: "))
        if self.t == 1:
            self.c3 = int(input("Value for c: "))

    def jInvariant(self):
        if self.t == 0:
            return 1/(self.c2)
        else:
            return 0


    def __str__(self):
        # Note: In the future, I will make sure that, when a constant is 1, the coefficient 
        # does not appear.
        if self.t == 0:
            return("y^2 + xy = x^3 + " + str(self.c1) + "x^2 + " + str(self.c2))
        else:
            return("y^2 + " + str(self.c1) + "y = x^3 + " + str(self.c2) + "x + " + str(self.c3))

    __repr__ = __str__
