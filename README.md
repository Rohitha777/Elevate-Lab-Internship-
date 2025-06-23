
# 🔢 Calculator CLI App

## 🚀 Objective
A simple command-line interface (CLI) calculator application written in Python. It allows users to perform basic arithmetic operations, view calculation history, and clear the history.

---

## 🛠️ Tools & Technologies

- **Language**: Python 3
- **Editor**: VS Code 
- **Interface**: Command-Line (Terminal)

---

## 📦 Features
- Basic operations: `+`, `-`, `*`, `/`
- Input validation and division-by-zero error handling
 - Perform Addition (+)
 - Perform Subtraction (-)
- Perform Multiplication (*)
- Perform Division (/) (with zero division error handling)
- View previous calculation history
- Clear the history
- Exit application

  
---

🔁**Loops**
Used to keep the calculator running continuously until the user types exit.
Enables repeated user input and interaction.

---

🧩**Functions**
Modular code structure with reusable functions:
add(a, b)
sub(a, b)
mul(a, b)
div(a, b)
Calculator() displays the menu, get_num() handles user input.

---

🔀 **Conditionals**
if/elif/else statements are used to:
Determine which operation the user selected
Handle special commands like history, clear, or invalid input
Prevent division by zero

----

**💬 CLI Interaction**
Uses input() and print() for user interaction in the terminal.
Provides real-time prompts and feedback for a smooth user experience.
Maintains a session-based history of calculations.

---
**📤 Sample Output**
--------- WELCOME TO CLI CALCULATOR ----------
Select an operation:
  +  Addition
  -  Subtraction
  *  Multiplication
  /  Division
 Type 'history'  Show previous calculations
 Type 'Clear' to clear History
 Type 'exit'  Close the calculator

Enter your choice: +
Enter First Number: 10
Enter Second Number: 5
Result: 15.0

Enter your choice: -
Enter First Number: 10
Enter Second Number: 3
Result: 7.0

Enter your choice: *
Enter First Number: 4
Enter Second Number: 2
Result: 8.0

Enter your choice: /
Enter First Number: 9
Enter Second Number: 3
Result: 3.0

Enter your choice: /
Enter First Number: 7
Enter Second Number: 0
Result: Zero Division Error

Enter your choice: history
-----CALCULATION HISTORY------
10.0 + 5.0 =15.0
10.0 - 3.0 =7.0
4.0 * 2.0 =8.0
9.0 / 3.0 =3.0
7.0 / 0.0 =Zero Division Error

Enter your choice: clear
----HISTORY CLEARED----

Enter your choice: history
-----No Calculations Yet-----

Enter your choice: exit
THANKS FOR USING CALCULATOR.BYE!!




