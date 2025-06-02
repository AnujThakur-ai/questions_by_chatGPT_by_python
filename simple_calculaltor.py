#to perform addition subtraction, multiplication and division
#take user input
num1 = float(input("enter 1st number:\t"))
num2 = float(input("enter 2nd number:\t"))

# get the choice from user
print(''' you have four option:
      1. addtion
      2. subtraction
      3.multiplication
      4. division
      other will directly terminate the program''')

#for additon
def addition(a,b):
        
        print(f"the sum of {num1} and {num2} is {num1+num2}")

def subtraction(num1, num2):

          
    print(f"the answer of {num1} and {num2} is {num1-num2}")
   
# product:
def multiply(num1, num2):
        print(f"the product of {num1} and {num2} is {num1*num2}")

#division
def divide(num1, num2):
    print(''' enter your choice for numenator and dinomentor 
             1. for num1 numentor
             2. for num2 numenator''')
    a= int (input("enter you choice:\t"))
    if a==1:
          print(f"answer: {num1/num2}")
    elif a==2:
          print(f"answer: {num2/num1}")
    else:
          print("invalid choice!!")
# main 

choice = int(input("enter your choice:\t"))

if choice ==1:
      print(addition(num1, num2))
      
elif choice  ==2:
      print(subtraction(num1 , num2))
      
elif choice ==3:
      print(multiply(num1, num2))
      
elif choice ==4:
      print(divide(num1, num2))
    
else:
      print("invalid choice")
      


          