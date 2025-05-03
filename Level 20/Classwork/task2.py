"""მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ თუ ეს რიცხვი დადებითია დაბეჭდეთ ეს და კიდევ შეამოწმეთ ლუწია თუ კენტი, ხოლო თუ არაა დადებითი მხოლოდ დაბეჭდეთ რომ უარყოფითია"""

number=int(input("enter number"))
if number > 0:
    print("positive")
    if number % 2 == 0:
        print("even")
    else:print("odd")
else:print("negative")
