# write a program that calculates the tip to be paid by each person

print("Wellcome to the tip calculator")
total = input("What was the total bill? $")
tip = input("How much tip would you like to give? ")
no_of_people = input("How many people to split the bill? ")

# convert the total to float
total = float(total)

# convert the tip and no_of_people to integer
tip = int(tip)
no_of_people = int(no_of_people)

#  calculate the total bill
total_bill = total + total * tip / 100

# calculate the bill per person
bill_per_person = total_bill / no_of_people

# round the bill per person to 2 decimal places
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(final_amount)
# this is another way to round to 2 decimal places which keeps 0 at the end even if the number is a whole number

# print the final amount
print(f"Each person should pay with tip: ${final_amount}")
