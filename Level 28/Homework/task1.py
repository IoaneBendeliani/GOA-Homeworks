"""lower(),
2) შემოიტანეთ სიტყვა input-ით და დაბეჭდეთ ის პატარა ასოებით

3) შემოიტანეთ ორი სიტყვა და შეადარეთ (print(word1 == word2) ისე, რომ არ ჰქონდეს მნიშვნელობა ასოების სიდიდეს (გამოიყენეთ lower)

4) მოცემული სიაა: ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]. ყველა ელემენტი გადააკეთეთ პატარა ასოებად და დაბეჭდეთ (გამოიყენეთ for ციკლი)"""

# 2) შემოიტანეთ სიტყვა და დაბეჭდეთ პატარა ასოებით
word = input("შეიყვანეთ სიტყვა: ")
print("პატარა ასოებით:", word.lower())

# 3) შემოიტანეთ ორი სიტყვა და შეადარეთ ისე, რომ არ ჰქონდეს მნიშვნელობა ასოების სიდიდეს
word1 = input("შეიყვანეთ პირველი სიტყვა: ")
word2 = input("შეიყვანეთ მეორე სიტყვა: ")
print("სიგრძის თვალსაზრისით ტოლია?", word1.lower() == word2.lower())

# 4) მოცემული სია გადააკეთეთ პატარა ასოებად და დაბეჭდეთ
countries = ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]
print("ქვეყნები პატარა ასოებით:")
for country in countries:
    print(country.lower())