# funcs with multiple args 
# ex 2 
#task1 take three numbers as args and return largest one 


def largest(x,y,z):
    if x>y and  x>z: # to check 1st is greater or not
        print("largest number is ",x )
    elif y > x and y > z:
        print("largest one is ",y)
    else:
        print("largest num is ",z) 

# taking user input of three integers
a = int(input("enter 1st number: ")) 
b = int(input("enter 2nd number: "))
c = int(input("enter 3rd number: ")) 
largest(a,b,c) #calling func 

#task2 - average of list 

def avg(list):
    w = 0 
    t = 0
    for i in list:
        w += i # for total 0f numbers in list
        t +=1 # to get the length of list 
        u = w/t 
    return w/t 

e = [1,2,3,4,5,6,7,8,9]
print(avg(e)) 
#task3 - to check number is prime or not 
def is_prime(o):
    if o <= 1: # to check give number is less than 1 or not
        return False 
    for j in range(2,int(o**0.5)+1):
        if o % j ==0:
            return False 
        return True 
    
qp = int(input("enter a number to check  : ")) 
print(is_prime(qp)) 