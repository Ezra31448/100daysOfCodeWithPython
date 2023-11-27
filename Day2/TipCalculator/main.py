# Constructor

# Output
print('Welcome to the tip calculator.')
total_bill = float(input('What was to total bill? $'))
percent_tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
divine_by = int(input('How many people to split the bill? '))

calculate_tip = (total_bill * int(percent_tip))/100
sum_total = float(total_bill) + calculate_tip
sum_total_per_person = round(sum_total / divine_by, 2)
# To prevent number might be 33.6 but we need 33.60
sum_total_per_person = "{:.2f}".format(sum_total_per_person) 


print(f'''Each person should pay : ${sum_total_per_person}''')