import tracker
status=True
while status:
    print(f"*********EXPENSE TRACKER*********")
    print("1.Add Expense")
    print("2.View Expense")
    print("3.Delete Expense")
    print("4.Search Expense")
    print("5.Show Total")
    print("6.Show Category Totals")
    print("7.Edit Expense")
    print("8.Today's Expense")
    print("9.Exit")   
    try:
       n=int(input("Enter your choice : "))
    except ValueError:
        print("Invalid input")
        continue
    match n:
        case 1:
            tracker.AddExpense()
        case 2:
            tracker.ViewExpense()
        case 3:
            tracker.DeleteRow()
        case 4:
            tracker.SearchByID()
        case 5:
            tracker.TotalAmount()
        case 6:
            tracker.CategoryTotals()
        case 7:
            tracker.EditExpense()
        case 8:
            tracker.ExpenseOfToday()
        case 9:
             status=False
        case _:
            print("Invalid input")
        
