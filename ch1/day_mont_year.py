# Number of days -> ...years, ...months, ...days

# Giving total days
total_days = int(input("Enter total days: "))

# Calculate the number of years
years = total_days // 365

# Calculate the remaining number of days (-years)
days_remaining = total_days - (years * 365)

# Calculate the number of months
months = days_remaining // 30

# Calculate the remaining days
days = days_remaining - (months * 30)

# Printing the result
print(f"{total_days} days is equivalent to {years} years, {months} months and {days} days.")