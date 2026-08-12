import datetime
import csv
File_Path="Python_Practice/expenseTracker/output.csv"
class Tracker:

    next_id=0
    
    def __init__(self,category,description,amount,date):
        self.category=category
        self.description=description
        self.amount=amount
        self.date=date

        Tracker.next_id+=1
        self.id=Tracker.next_id
        

try:
     with open(File_Path,"r") as file:
          content=csv.reader(file)
          for line in content:
                 Tracker.next_id=max(Tracker.next_id,int(line[0]))

except FileNotFoundError:
            pass    


def AddExpense():
        print(f"*********Add Expense**********")
        ctgy=input("Enter the category(F/T/B/A) :").upper()
        des=input("Description : ")
        amnt=float(input("Enter the amount : "))
        today=datetime.datetime.now().strftime("%d-%m-%Y")
        expense=Tracker(ctgy,des,amnt,today)

        print("==============================")
        print("Added new Expense :")
        print(f"id = {expense.id}")
        print(f"category = {expense.category} ")
        print(f"description = {expense.description}")
        print(f"amount = {expense.amount}")
        print(f"Date = {expense.date}")
        print("==============================")

        tracks=[expense.id,expense.category,expense.description,expense.amount,expense.date]
        

        with open(File_Path,"a",newline="") as file:
             writer=csv.writer(file)
             writer.writerow(tracks)


def VeiwExpense():
        
        with open(File_Path,"r",newline="") as file:
              content=csv.reader(file)
              print("*********************Your Expenses************************")
              print(f"{'ID':<5}{'CATEGORY':<12}{'DESCRIPTION':<20}{'AMOUNT':<12}{'DATE':<15}")
              for line in content:
                    print(f"{line[0]:<5}{line[1]:<12}{line[2]:<20}{line[3]:<12}{line[4]:<15}")
              print("**********************************************************")


def TotalAmount():
        
        with open(File_Path,"r",newline="") as file:
                content=csv.reader(file) 
                print(f"PAYMENTS :")
                total=0
                for line in content:
                      print(f"{line[3]} Tk")
                      total+=float(line[3])
                print(f"Total amount : {total} Tk")
def SearchByID():
       ID=int(input("Enter the id of the expense you want to search : "))
       found=False
       
       with open(File_Path,"r",newline="") as file:
              content=csv.reader(file)
              for line in content:
                     if ID==int(line[0]):
                            found=True
                            print(f"{'ID':<5}{'CATEGORY':<12}{'DESCRIPTION':<20}{'AMOUNT':<12}{'DATE':<15}")
                            print(f"{line[0]:<5}{line[1]:<12}{line[2]:<20}{line[3]:<12}{line[4]:<15}")
                            break
       if  found==False:
              print(f"{ID} not found!")

def DeleteRow():
       delete_ID=int(input("Enter the id of the expense you want to delete : ")) 
       
       rows=[]
       found=False
       with open(File_Path,"r",newline="") as file:
            content=csv.reader(file)
            for line in content:
                   if line:
                    if int(line[0])==delete_ID:
                          found=True      
                    else:
                          rows.append(line)
                   
       with open(File_Path,"w",newline="")as file:
              writer=csv.writer(file)
              writer.writerows(rows)
       if not found:
             print(f"{delete_ID} not found")
       else:
             print("Expense deleted!")