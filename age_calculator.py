from datetime import date

def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year


    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age -= 1

    return age


year = int(input("Enter your birth year (YYYY): "))
month = int(input("Enter your birth month (MM): "))
day = int(input("Enter your birth day (DD): "))


birthdate = date(year, month, day)


age = calculate_age(birthdate)

print(f"You are {age} years old.")
