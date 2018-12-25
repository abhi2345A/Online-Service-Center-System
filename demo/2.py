
class Sum:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def sum(self):
        print('Sum of numbers is:{}'.format(self.num1+self.num2))


if __name__=='__main__':
    # Use input function to input the values but by default it inputs a string,so typecast the values to int
    num1 = int(input('Enter First Number:'))
    num2 = int(input('Enter Second Number:'))
    obj = Sum(num1,num2)
    obj.sum()





