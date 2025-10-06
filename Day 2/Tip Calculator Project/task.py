print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

share_per_person= (bill/people)* ((100+12)/100)

print(round(share_per_person, 2))


