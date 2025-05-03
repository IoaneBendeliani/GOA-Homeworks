"""score=int(input("enter your score"))

if score > 80:
    print("A")
if score > 60 and score < 80:
    print("B")"""
score = int(input("Enter your score: "))

got_A = False
if score > 80:
    print("A")
    got_A = True
if score > 60 and score <= 80:
    print("B")