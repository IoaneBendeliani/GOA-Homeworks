#შექმენით პროგრამა რომელიც მომხმარებელს შეეკითხება პაროლს სანამ ის არ შემოიყვანს goabest123-ს

correct_password = "goabest123"

while True:
    user_input = input("please enter password: ")
    if user_input == correct_password:
        print("password correct!")
        break
    else:
        print("password invalid try again")