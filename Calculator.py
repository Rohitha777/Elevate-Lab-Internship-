#Task 1 :Build a Calculator CLI App

#Function for Addition
def add(a,b):
    return a+b 
#Function for Subtraction
def sub(a,b):
    return a-b 
#Function for Multiplication
def mul(a,b):
    return a*b 
#Function for Division
def div(a,b):
    if b==0:
        return "Zero Division Error"
    return a/b 

#Display menu options to users
def Calculator():
    print("--------- WELCOME TO CLI CALCULATOR----------")
    print("Select an operation:")
    print("  +  Addition")
    print("  -  Subtraction")
    print("  *  Multiplication")
    print("  /  Division")
    print(" Type 'history'  Show previous calculations")
    print("Type 'Clear' to clear History")
    print("Type 'exit'  Close the calculator")

# Get valid number input from the user
def get_num(prompt):
    while True:
        try:
            return float(input(prompt))  # Try to convert user input to float
        except ValueError:
            print("Please enter a valid number.")  # Handle invalid input


def main():
    history=[]
    while True:
        Calculator()
        choice=input("Enter your choice: ").strip()
        # Show all previous calculations
        if choice.lower()=='history':
            if history:
                print("-----CALUCLATION HISTORY------")
                for cal in history:
                    print(cal)
            else:
                print("-----No Calculations Yet-----")
                continue 
        #Clear the history of calculator
        elif choice.lower()=='clear':
            history.clear()
            print("----HISTORY CLEARED----")
            continue
        #exit the calculator
        elif choice.lower()=='exit':
            print("THANKS FOR USING CALCULATOR.BYE!!")
            break
        # To perform calculations
        elif choice in ("+","-","*","/"):
            x=get_num("Enter First Number: ")
            y=get_num("Enter Second Number: ")
            if choice=="+":
                result=add(x,y)
                exp=f"{x} + {y} ={result}"
            elif choice=='-':
                result=sub(x,y)
                exp=f"{x} - {y} ={result}"
            elif choice=='*':
                result=mul(x,y)
                exp=f"{x} * {y} ={result}"
            elif choice=="/":
                result=div(x,y)
                exp=f"{x} / {y} ={result}"

            print("Result:", result)  # Show result to user
            history.append(exp)  # Save to history
        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")

# Only run main() if this file is executed directly
if __name__ == "__main__":
    main()








