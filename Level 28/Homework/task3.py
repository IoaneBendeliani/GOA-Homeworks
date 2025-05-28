"""capitalize(),
8) შემოიტანეთ წინადადება input-ით და გამოიყენეთ capitalize ისე, რომ მხოლოდ პირველი ასო დარჩეს დიდი

9) მოცემული სტრინგია "gEoRGia". გადააკეთეთ ისე, რომ მხოლოდ პირველი ასო იყოს დიდი, დანარჩენი კი პატარა

10) მოცემული სიაა: ["georgia", "aRMENIA", "greeCE"]. ყველა ელემენტს ჯერ გაუკეთეთ lower, შემდეგ capitalize და დაბეჭდეთ#"""

# 8) შემოიტანეთ წინადადება და გამოიყენეთ capitalize
sentence = input("შეიყვანეთ წინადადება: ")
print("capitalize:", sentence.capitalize())

# 9) სტრინგი "gEoRGia" გადააკეთეთ მხოლოდ პირველი ასო დიდი, დანარჩენი პატარა
name = "gEoRGia"
fixed_name = name.capitalize()
print("დასწორებული სახელი:", fixed_name)

# 10) სია გადააკეთეთ lower და შემდეგ capitalize
countries = ["georgia", "aRMENIA", "greeCE"]
print("სია capitalize ფორმატში:")
for country in countries:
    print(country.lower().capitalize())