#შექმენით პროგრამა while ციკლით რომელიც მომხარებელს შეეკითხება pin კოდს (4 ციფრიანი კოდი) იქამდე სანამ არ შემოიყვანს სწორად, საბოლოოდ დაუბეჭდეთ რომ გაიარა ავტორიზაცია და გამოუტანეთ თუ რამდენი ცდა დასჭირდა

correct_pin = "1234"

attempts = 0


while True:
    pin_input = input("please enter your PIN: ")
    attempts += 1  
    if pin_input == correct_pin:
        print(f"authentication complete.")
        print(f"your attempts: {attempts}")
        break 
    else:
        print("wrong PIn try again.")