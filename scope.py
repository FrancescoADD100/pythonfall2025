"""
    Return statements and scope

"""
def weekdays():

    work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    weekend = ["Saturday", "Sunday"]
    return work_days, weekend # Local variables inside of weekdays



def main():

    days, weekend = weekdays() # Scope is inside of main
    print("work Week")
    days.append("Saturday")
    for day in days:
        print(day)

    print("\nWeekend")
    for day in weekend:
        print(day)



main()
