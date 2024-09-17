from datetime import datetime
#function to calculate age in years and days
def calculae_age(birth_date):
    today = datetime.today()
    age_in_days = (today - birth_date).days
    age_in_years =age_in_days // 365 
    #appropriate calculation 
    remaining_days = age_in_days % 365
    return age_in_years, remaining_days

#input from the users
birth_day = int(input("Enter your birthdate:"))
birth_month = int(input("Enter your birth month:"))
birth_year = int(input("Enter your birth year:"))

#create a datetime object for the birth date
birth_day = datetime(birth_year,birth_month,birth_day)

#calculate age
year,days = calculae_age(birth_date)
print(f"you are {year} year and {days} days old")



