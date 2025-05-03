"""შექმენით ცივი სასმელების სია აქედან ერთ-ერთი ელემენტი უნდა ეწეროს ცვლადის სახით, შემდეგ მომხმარებელს შემოტანინეთ 1 ცივი სასმელი რომელსაც დაამატებთ თქვენს მაცივარში. შემდეგ მომხარებელს უნდა შემოატანინოთ არჩევანი ამ სასმელებიდან და სიიდან ელემენტის წამოღების indexing method-ის საშვალებით გამოუტანეთ ეს სასმელი. შექმენით ცვლადი რომელშიც შეინახავთ თქვენს სახელს, გამოიტანეთ ამ სტრინგიდან თქვენთვის სასურველი 3 სიმბოლო"""

my_drink="beer"
customer_drink=input("choose your drink:")

cold_drinks=["ice tea", "ice coffe", "orange juice", "apple juice", my_drink , customer_drink]
choice=int(input("choose your drink:"))

print(cold_drinks)
print(choice)