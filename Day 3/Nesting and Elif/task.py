print("Welcome to the rollercoaster!")
maths_score = int(input("What is your maths score "))
english_score = int(input("What is your english score "))

if maths_score >= 90:
    if english_score >= 90:
        print("You're good at everything")
    else:
        print("You're good at maths")
else:
    if english_score >= 90:
        print("You're good at english")
    else:
        print("You are good at neither english nor maths")