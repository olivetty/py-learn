my_list = [10, 20, 30, 40, 50]


def days_to_hours(days):
    hours_in_month = days * 24
    print(f"There are {hours_in_month} hours in {days} days")

for days_in_list in my_list:
    days_to_hours(days_in_list)