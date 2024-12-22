while True:
    task = input("Enter your task:")
    priority = input("Priority (high/medium/low):")
    time_bound = input("Is it time-bound? (yes/no):")
    match task:
        case "Finish project report":
            if priority == "high":
             if time_bound == "yes":
                print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
        case "Read a book":
          if priority == "low":
             if time_bound == "no":
               print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
        case "Make lunch":
          if priority == "medium":
             if time_bound == "no":
                print("Reminder: 'Make lunch' is a medium priority task. Consider making time for it.") 
        case _:
          print("Invalid task entered.")             

            

    