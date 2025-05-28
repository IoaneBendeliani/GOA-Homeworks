"""შექმენით პროგრამა, რომელიც მოხმარებელს მოსთხოვს წინდადების შეყვანას, შემდეგ კი ამ წინადადებას სამჯერ დაბეჭდავს სხვადასხვა სახით: lower, upper, capitalize ფორმატებში"""

sentence = input("შეიყვანეთ წინადადება: ")

print("პატარა ასოებით:")
print(sentence.lower())

print("დიდი ასოებით:")
print(sentence.upper())

print("პირველი ასო დიდი, დანარჩენი პატარა:")
print(sentence.capitalize())