
class Math:

    # init method or constructor
    def __init__(self ,a ,b):
        self._product = (a*b)
        self._sum = (a+b)
        self._productdigits = self.ProductDigits()
        self._sumdigits = self.SumDigits()




    def ProductDigits(self) :
        count = 0

        # absolute value of the
        # product of two numbers
        p = abs(a * b)

        # if product is 0
        if (p == 0) :
            return 1

        # count number of digits
        # in the product 'p'
        while (p > 0) :
            count = count + 1
            p = p // 10


        # required count of digits
        return count



    def SumDigits(self) :
        count2 = 0

        # absolute value of the
        # sum of two numbers
        p = abs(a + b)

        # if sum is 0
        if (p == 0) :
            return 1

        # count number of digits
        # in the sum 'p'
        while (p > 0) :
            count2 = count2 + 1
            p = p // 10


        # required count of digits
        return count2

    @property
    def product(self):
        return self._product

    @property
    def sum(self):
        return self._sum

    @property
    def sum_digits(self):
        return self._sumdigits

    @property
    def product_digits(self):
        return self._productdigits



# Driver program to test above
a = 74
b = 200
math = Math(a,b)
print(f"{a} times {b} = {math.product} & Number of digits is {math.product_digits}")
print(f"{a} plus {b} = {math.sum} & Number of digits is {math.sum_digits}")
