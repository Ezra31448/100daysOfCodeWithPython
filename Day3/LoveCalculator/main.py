print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
lower_name1 = name1.lower()
lower_name2 = name2.lower()

count_1 = 0 #count for first position
count_2 = 0 #count for second position 

#count for first position
count_1 += lower_name1.count("t")
count_1 += lower_name1.count("r")
count_1 += lower_name1.count("u")
count_1 += lower_name1.count("e")

count_1 += lower_name2.count("t")
count_1 += lower_name2.count("r")
count_1 += lower_name2.count("u")
count_1 += lower_name2.count("e")

#count for second position 
count_2 += lower_name1.count("l")
count_2 += lower_name1.count("o")
count_2 += lower_name1.count("v")
count_2 += lower_name1.count("e")

count_2 += lower_name2.count("l")
count_2 += lower_name2.count("o")
count_2 += lower_name2.count("v")
count_2 += lower_name2.count("e")

#sum score for if_else statement
sum_score = (count_1 * 10) + count_2

if (sum_score >= 40 and sum_score <= 50):
    print(f'Your score is {sum_score}, you are alright together.')
elif (sum_score < 10 or sum_score > 90):
    print(f'Your score is {sum_score}, you go together like coke and mentos.')
else:
    print(f'Your score is {sum_score}.')