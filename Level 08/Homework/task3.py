"""დაწერეთ პითონის კოდი რომელიც მომხმარებელს input-ის საშვალებით შეეკითხება და ცვლადში შეინახავს შემდეგ ინფორმაციას:
Name
Surname
Age
Location
Occupation
Hobby
ამ ცვლადების საშვალებით კი გამოიტანს ერთ წინადადებას რომელშიც ყველა მიღებული ინფორმაცია იქნება გამოყენებული. """

Name=input("Your name")
Surname=input("Your surname")
Age=input("Your age")
Location=input("location")
Occupation=input("your occupation")
Hobby=input("your hobby")

print(Name + " " + Surname + " " + "is" + " " + Age + " " + "years old" + " " + "lives in" + " " + Location + " " + "is occupied by" + " " + Occupation + " " + "enjoys" + " " + Hobby)