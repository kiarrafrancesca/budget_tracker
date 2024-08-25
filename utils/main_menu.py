from utils.system import System

system = System()

def main_menu():
    while True:
        try:
            print("==================================================")
            print("               Budget Management System")
            print("==================================================")
            print("                 [1] Add Income")
            print("                 [2] Add Expense")
            print("                 [3] Set Budget")
            print("                 [4] Set Savings Goal")
            print("                 [5] Budget Expenses ")
            print("--------------------------------------------------")
            print("                 [6] Exit")
            print("==================================================")

            choice = int(input(" Enter your choice: "))

            if choice == 1:
                system.clear_screen()
                system.income()
            elif choice == 2:
                system.clear_screen()
                system.expenses()
            elif choice == 3:
                system.clear_screen()
                system.budget()
            elif choice == 4:
                system.clear_screen()
                system.savings_goal()
            elif choice == 5:
                system.clear_screen()
                system.budget_system()
            elif choice == 6:
                system.clear_screen()
                print("Exiting...")
                quit()
            else:
                print("Please enter a valid option from the menu.")
            
        except ValueError:
            print("Please enter a valid option from the menu.")