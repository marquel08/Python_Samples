print("Welcome to my Lakers quiz! ")

playing =input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play :)")
score = 0
    
answer = input("Who wore number 9 in 1998 for the Lakers? ")
if answer.lower() == "nick van exel":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("How many championships have the Lakers won? ")
if answer.lower() == "17":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("Which Kobe Bryant's jersey number(s) is retired? ")
if answer.lower() == "24 and 8":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("What was Kobe Bryant's first jersey number? ")
if answer.lower() == "8":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("Who was the most dominant Center for the Lakers? ")
if answer.lower() == "shaq":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score/5) * 100) + "%.")