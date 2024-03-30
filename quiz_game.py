#This is my first Python project. I can add more questions to the "Quiz_Game", for now this is what it is.


print("Welcome to the quiz game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GUI stand for? ").lower()
if answer == "graphical user interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What does SSD stand for? ").lower()
if answer == "solid state drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does HDD stand for? ").lower()
if answer == "hard disk drive":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does TPM ? ").lower()
if answer == "trusted platform module":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does CMOS stand for? ").lower()
if answer == "complementary metal oxide semiconductor":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does DDR stand for? ").lower()
if answer == "double data rate":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does ISO stand for? ").lower()
if answer == "optical disk image":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")






print("You got " + str(score) + " Questions Correct! ")
print("You got " + str((score/11) * 100) + "%.")


