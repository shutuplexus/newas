# func with return values 
#task1 reverse string  
def reverse_string(r):
    return r[::-1] # to reverse 
i = str(input("rnter a string : ")) # taking input from user 
print(reverse_string(i)) # calling the func 

def reverse_string(x,y):
    u = 0 
    for i in x:
        if i == y: 
            u += 1 # to count same chars 
    return u


m = str(input("rnter a string : ")) # taking input from user (string)
n = str(input("rnter a char : ")) # taking input from user (char)
print(reverse_string(m,n)) # calling the func 


