#მომხმარებელს იქამდე შეეკითხეთ რიცხვები სანამ უარყოფით რიცხვს არ შემოიყვანს, while ციკლისა და input ინსტრუქციის საშვალებით, ასევე პირობითი განცხადებების დადებითობა/უარყოფითობის შესამოწმებლად, საბოლოოდ დაბეჭდეთ ყველა მიღებული დადებითი რიცხვის ჯამი

positive_sum = 0

while True:
    number = int(input("Enter a number (negative number to stop): "))
    
    if number < 0:
        break 

    if number > 0:
        positive_sum += number  

print("Sum of all positive numbers entered:", positive_sum)