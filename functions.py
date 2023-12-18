def days_to_hours(days):
    hours_in_month = days * 24
    print(f"There are {hours_in_month} hours in {days} days")

def work_days_to_hours(days):
    work_hours_in_month = days * 8
    print(f"There are {work_hours_in_month} working hours in {days} work days")

days_to_hours(365)
work_days_to_hours(21)