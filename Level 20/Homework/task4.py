#მომხმარებელს 3 მცდელობა აქვს სწორი PIN კოდის შეყვანისთვის. თუ შეიყვანს სწორად, დაიბეჭდება "Access Granted", სხვა შემთხვევაში "Access Denied" გამოიყენეთ პირობითი განცხადებები

correct_pin = "1234"

attempts = 3

while attempts > 0:
    pin = input("Enter your PIN: ")
    
    if pin == correct_pin:
        print("Access Granted")
        break 
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect PIN. You have {attempts} attempt(s) left.")
        else:
            print("Access Denied")