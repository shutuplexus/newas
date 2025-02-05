# basic funcs 
# ex1
# task 1- program to calculate area of circle by taking radius as input 

def area_of_circle(r):
    area = 3.14*2*r*r # formula 
    print(area) # output

a = int(input("Enter radius : ")) # taking input from user
area_of_circle(a) # calling the func with passing the argument


# task 2 
def power_of_number(x,y):
    z = x**y # formula 
    print(z)

w = int(input("enter a base: ")) 
t = int(input("enter exponent: ")) 
power_of_number(w,t)

#task 3 celsius to farenheit 

def celsius_to_farenheit(celsius):
   u = (celsius*9/5)+32 #formula to convert 
   print(u) 

w = int(input("enter a celsius: "))
celsius_to_farenheit(w) 