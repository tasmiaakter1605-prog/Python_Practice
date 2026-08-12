class Tracker:

    next_id=0
    
    def __init__(self,category,description,amount,date):
        self.category=category
        self.description=description
        self.amount=amount
        self.date=date

        Tracker.next_id+=1
        self.id=Tracker.next_id