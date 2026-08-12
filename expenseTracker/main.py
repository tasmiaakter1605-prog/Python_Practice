import tracker
status=True
while status:
    print(f"*********EXPENSE TRACKER*********")
    print("1.Add Expense")
    print("2.Veiw Expense")
    print("3.Delete Expense")
    print("4.Search Expense")
    print("5.Show Total")
    print("6.Exit")   

    n=int(input("Enter your choice : "))
    match n:
        case 1:
            tracker.AddExpense()
        case 2:
            tracker.VeiwExpense()
        case 3:
            tracker.DeleteRow()
        case 4:
            tracker.SearchByID()
        case 5:
            tracker.TotalAmount()
        case 6:
             status=False