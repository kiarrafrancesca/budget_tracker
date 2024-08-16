import os

class System:
    def __init__(self):
        self.housing = 0.0
        self.ebill = 0.0
        self.wbill = 0.0
        self.ibill = 0.0
        self.grocery = 0.0
        self.ent = 0.0
        self.misc = 0.0

        self.housing_budg = 0.0
        self.ebill_budg = 0.0
        self.wbill_budg = 0.0
        self.ibill_budg = 0.0
        self.grocery_budg = 0.0
        self.ent_budg = 0.0
        self.misc_budg = 0.0

        self.housing_calc = 0.0
        self.ebill_calc = 0.0
        self.wbill_calc = 0.0
        self.ibill_calc = 0.0
        self.grocery_calc = 0.0
        self.ent_calc = 0.0
        self.misc_calc = 0.0

        self.monthly_income = 0.0
        self.total_expenses = 0.0
        self.total_budget = 0.0
        self.sgoal = 0.0
        self.total = 0.0

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def press_return(self):
        input("Press 'enter' to return.")
        self.clear_screen()
        
    def income(self):
        print("------------------------------")
        self.monthly_income = float(input(" Monthly Income: "))

    def expenses(self):
        print("----------------------------------------")
        print("          Input your expenses")
        print("----------------------------------------")
        self.housing = float(input(" Housing: "))
        self.ebill = float(input(" Electric Bill: "))
        self.wbill = float(input(" Water Bill: "))
        self.ibill = float(input(" Internet Bill: "))
        self.grocery = float(input("Grocery: "))
        self.ent = float(input("Entertainment: "))
        self.misc = float(input(" Miscellaneous: "))

        self.total_expenses = self.housing + self.ebill + self.wbill + self.ibill + self.grocery + self.ent + self.misc

        print("----------------------------------------")
        print(f" Total Expenses: {self.total_expenses}")

    def budget(self):
        print("----------------------------------------")
        print("               Set Budget")
        print("----------------------------------------")
        self.housing_budg = float(input(" Housing: "))
        self.ebill_budg = float(input(" Electric Bill: "))
        self.wbill_budg = float(input(" Water Bill: "))
        self.ibill_budg = float(input(" Internet Bill: "))
        self.grocery_budg = float(input("Grocery: "))
        self.ent_budg = float(input("Entertainment: "))
        self.misc_budg = float(input(" Miscellaneous: "))

        self.total_budget = self.housing_budg + self.ebill_budg + self.wbill_budg + self.ibill_budg + self.grocery_budg + self.ent_budg + self.misc_budg

        print("----------------------------------------")
        print(f" Total Expenses: {self.total_budget}")

        if self.monthly_income == 0.0:
            print("\nYou have not set an income.")
        elif self.total_budget > self.monthly_income:
            print("\nYour budget is insufficient.")
        else: 
            print("\nYou have enough budget.")

    def savings_goal(self):
        print("------------------------------")
        self.sgoal = float(input(" Savings Goal: "))

    def budget_system(self):
        self.housing_calc = self.housing_budg - self.housing
        self.ebill_calc = self.ebill_budg - self.ebill
        self.wbill_calc = self.wbill_budg - self.wbill
        self.ibill_calc = self.ibill_budg - self.ibill
        self.grocery_calc = self.grocery_budg - self.grocery
        self.ent_calc = self.ent_budg - self.ent
        self.misc_calc = self.misc_budg - self.misc

        self.total = self.housing_calc + self.ebill_calc + self.wbill_calc + self.ibill_calc + self.grocery_calc + self.ent_calc + self.misc_calc

        print("==================================================================================")
        print("                            Budget Management System")
        print("==================================================================================")
        print("     CATEGORY     |     BUDGET     |     SPENT     |     OVER/UNDER     ")
        print(f" Housing:           {self.housing_budg}     {self.housing}      {self.housing_calc}")
        print(f" Electric Bill:     {self.ebill_budg}       {self.ebill}        {self.ebill_calc}")
        print(f" Water Bill:        {self.wbill_budg}       {self.wbill}        {self.wbill_calc}")
        print(f" Internet Bill:     {self.ibill_budg}       {self.ibill}        {self.ibill_calc}")
        print(f" Grocery:           {self.grocery_budg}     {self.grocery}      {self.grocery_calc}")
        print(f" Entertainment:     {self.ent_budg}         {self.ent}          {self.ent_calc}")
        print(f" Miscellaneous:     {self.misc_budg}        {self.misc}         {self.misc_calc}")
        print("----------------------------------------------------------------------------------")
        print(f" TOTAL:             {self.total_budget}     {self.total_expenses}       {self.total}")
        print("==================================================================================")

        if self.total >= self.sgoal:
            print(f"\nYou have met your savings goal ({self.sgoal}). You saved: {self.total}")
        else:
            print(f"\nYou are below your savings goal ({self.sgoal}). You are short {self.sgoal - self.total}")

        self.press_return()

