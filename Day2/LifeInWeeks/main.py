# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:

# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input
# 56
# Example Output
# You have 1768 weeks left.

# There are 365 days in a year, 
# 52 weeks in a year and 12 months in a year.

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
cal_week = int(age)*52
week_left = 90*52
cal_left = week_left - cal_week
print(f'''You have {cal_left} weeks left.''')