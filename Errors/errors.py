#syntax error
# print(1)
# int(5) #int 5
# int (4)
# print(2) # print 2
# a=[1,2,4] # a=[2,)
# print (a)

  #Exception
# a = 1
# b= "2"
# print(int(2.5))
# print (a/0) #ZeroDivisionError: division by zero

def divide(a,b):
    try:
       return a/b
    except:
        return "You are dividing by zero"   
print(divide(1,3))
print("end of program")