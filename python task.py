from datetime import datetime

# Function to calculate age in years and days
def calculate_age(birth_date):
    today = datetime.today()
    age_in_days = (today - birth_date).days
    age_in_years = age_in_days // 365  # Approximate calculation
    remaining_days = age_in_days % 365
    return age_in_years, remaining_days

# Input from the user
birth_day = int(input("Enter your birth day: "))
birth_month = int(input("Enter your birth month: "))
birth_year = int(input("Enter your birth year: "))

# Create a datetime object for the birth date
birth_date = datetime(birth_year, birth_month, birth_day)

# Calculate age
years, days = calculate_age(birth_date)

print(f"You are {years} years and {days} days old.")
