#შექმენით პროგრამა რომელშიც მომხმარებელმა უნდა შეიყვანოს რიცხვები, სანამ უარყოფითს არ შეიყვანს. დაბეჭდეთ შეყვანილი ლუწი და კენტი რიცხვების რაოდენობა გამოიყენეთ პირობითი განცხადებები

even_count = 0
odd_count = 0

while True:
    number = int(input("Enter a number (negative to stop): "))

    if number < 0:
        break  
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Count of even numbers:", even_count)
print("Count of odd numbers:", odd_count)