import datetime
import csv
import expense
File_Path="Python_Practice/expenseTracker/output.csv"

        

try:
     with open(File_Path,"r") as file:
          content=csv.reader(file)
          for line in content:
                 expense.Tracker.next_id=max(expense.Tracker.next_id,int(line[0]))

except FileNotFoundError:
            pass    


def AddExpense():
        print(f"*********Add Expense**********")
        while True:
              ctgy=input("Enter the category(F/T/B/A) :").upper()
              if ctgy in ["F","T","A","B"]:
                    break
              print("Invalid input,try again")
        des=input("Description : ")
        try:
         amnt=float(input("Enter the amount : "))
        except ValueError:
              print("Invalid input")
        today=datetime.datetime.now().strftime("%d-%m-%Y")
        Expense=expense.Tracker(ctgy,des,amnt,today)

        print("==============================")
        print("Added new Expense :")
        print(f"id = {Expense.id}")
        print(f"category = {Expense.category} ")
        print(f"description = {Expense.description}")
        print(f"amount = {Expense.amount}")
        print(f"Date = {Expense.date}")
        print("==============================")

        tracks=[Expense.id,Expense.category,Expense.description,Expense.amount,Expense.date]
        

        with open(File_Path,"a",newline="") as file:
             writer=csv.writer(file)
             writer.writerow(tracks)


def ViewExpense():
        
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
       try:
            ID=int(input("Enter the id of the expense you want to search : "))
       except ValueError:
             print("Invalid input")
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
       try:
            delete_ID=int(input("Enter the id of the expense you want to delete : ")) 
       except ValueError:
             print("Invalid input")
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

def EditExpense():
      while True:
            try:
                choice=int(input("Enter the ID to change : "))
            except ValueError:
                  print("Invalid ID")
                  continue
            found=False
            rows=[]
            with open(File_Path,"r",newline="")as file:
                  content=csv.reader(file)
                  for line in content:
                        if not line:
                              continue
                        if int(line[0])==choice:
                              found=True
                              print("Current Expense :")
                              print(f"Category    : {line[1]}")
                              print(f"Description : {line[2]}")
                              print(f"Amount      : {line[3]}")
                              print(f"Date        : {line[4]}")
                              
                              while True:
                                print("What do you want to change ?")
                                print("1.Category(C)")
                                print("2.Description(D)")
                                print("3.Amount(A)")
                                print("4.Cancel(X)")
                                change=input().upper()
                                if change=="C":
                                    line[1]=input("Enter new category : ").upper()
                                    break
                                elif change=="D":
                                    line[2]=input("Enter new description : ")
                                    break
                                elif change=="A":
                                    try:
                                     line[3]=float(input("Enter new amount : "))
                                     break
                                    except ValueError:
                                          print("Invalid input")
                                elif change=="X":
                                    return
                                else:
                                    print("Invalid input please try again")
                        rows.append(line)
            if not found:
                  print("ID not found")
                  return
            with open(File_Path,"w",newline="") as file:
                  writer=csv.writer(file)
                  writer.writerows(rows)
            print("Expense updated!")
            return

                  
                        

                  
def CategoryTotals():
      foodTotal=0
      transportTotal=0
      billTotal=0
      additionalTotal=0
      with open(File_Path,"r") as file:
            content=csv.reader(file)
            for line in content:
                  if line[1]=="F":
                        foodTotal+=float(line[3])
                  if line[1]=="T":
                        transportTotal+=float(line[3])
                  if line[1]=="B":
                        billTotal+=float(line[3])
                  if line[1]=="A":
                        additionalTotal+=float(line[3])
      print("TOTAL AMOUNT (CATEGORY-WISE)")
      print(f"Food       = {foodTotal}")
      print(f"Transport  = {transportTotal}")
      print(f"Bill       = {billTotal}")
      print(f"Additional = {additionalTotal}")

def ExpenseOfToday():
      Today=datetime.datetime.today().strftime("%d-%m-%Y")
      total=0
      with open(File_Path,"r")as file:
            content=csv.reader(file)
            for line in content:
                  if Today==line[4]:
                        total+=float(line[3])
      print(f"Expense of {Today} :")
      print(f"{total} Tk")

