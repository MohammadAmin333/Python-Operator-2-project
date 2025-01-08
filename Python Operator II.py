# Email Validation
username="Admin"
email="***@gmail.com"
if username=="Admin" or email=="***@gmail.com":
    print("You are successfully Logged in")
else:
    print("Parmission Denied")


username="Admin"
password="Admin123"
if username=="Admin" and password=="Admin123":
        print("Successfully Login")
else:
        print("Parmission Denied")

        

# Cricket Players Performance Evaluation

print("Cricket Players Performance Evaluation")
print("Press 1 to judge a player or press 2 to exit")
choice=int(input("Enter your choice:"))
if choice==1:
    runs=int(input("Enter the total runs scored by the player:"))
    matches=int(input("Enter the total matches player by the player:"))
    if runs> 500 and matches>10:
      print("Excellent player")
    elif runs>300 and matches>5:
      print("Good player")
    elif runs>100 and matches>2:
      print("Need To Improve")
    else:
      print("Average player")
elif choice==2:
    print("Exeting the program. Good Bye!!")
else:
    print("Invalid Input")            
      
    

    #Mark Sheet

mark = int(input("Enter the mark: "))  

if mark >= 80 and mark <= 100:  
    print("You got A+")  
elif mark >= 70 and mark < 80:  
    print("You got A")  
elif mark >= 60 and mark < 70:  
    print("You got B+")  
elif mark >= 50 and mark < 60:  
    print("You got B")  
elif mark >= 40 and mark < 50:  
    print("You got C")  
elif mark >= 33 and mark < 40:  
    print("You got D")  
else:  
    print("You are Fail.")  

# BMI Calculator

h=int(input("Height: "))
w=int(input("Weight: "))
bmi=w/(h*h)  
if bmi < 18.5:  
    print(f"your bmi is {bmi} and you are Underweight")  
elif bmi >= 18.5 and bmi < 24.9:  
    print(f"your bmi is {bmi} and you are healthy")  
elif bmi >= 24.9 and bmi < 29.9:  
    print(f"your bmi is {bmi} and you are healthy")  
elif bmi >= 29.9 and bmi < 34:  
    print(f"your bmi is {bmi} and you are Obese")  
else:
    print(f"your bmi is {bmi} and you are Extremely Obese")
