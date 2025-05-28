"""find(),
11) შემოიტანეთ სიტყვა input-ით და მოძებნეთ ასო a-ს პირველი პოზიცია

12) მოცემული სტრინგია "I visited Georgia, Armenia and Greece". მოძებნეთ Armenia და დაბეჭდეთ მისი პოზიცია

13) შექმენით სტრინგი და შემოიტანეთ საძიებელი სიტყვა input-ით. თუ სიტყვა მოიძებნება find-ით, დაბეჭდეთ პოზიცია, სხვა შემთხვევაში კი დაბეჭდეთ word not found"""

# 11) შემოიტანეთ სიტყვა და მოძებნეთ 'a'-ს პირველი პოზიცია
word = input("შეიყვანეთ სიტყვა: ")
pos_a = word.find('a')
if pos_a != -1:
    print(f"პოზიცია ასო 'a'-ს არის: {pos_a}")
else:
    print("ასო 'a' სიტყვაში ვერ მოიძებნა.")

# 12) სტრინგში "I visited Georgia, Armenia and Greece" მოძებნეთ "Armenia" და დაბეჭდეთ პოზიცია
text = "I visited Georgia, Armenia and Greece"
pos_armenia = text.find("Armenia")
if pos_armenia != -1:
    print(f"'Armenia'-ს პოზიცია ტექსტში არის: {pos_armenia}")
else:
    print("'Armenia' ტექსტში ვერ მოიძებნა.")

# 13) შექმენით სტრინგი და შემოიტანეთ საძიებელი სიტყვა. თუ მოიძებნება, დაბეჭდეთ პოზიცია, სხვაგვარად - word not found
my_text = "This is a sample string for searching."
search_word = input("შეიყვანეთ საძიებელი სიტყვა: ")
pos = my_text.find(search_word)
if pos != -1:
    print(f"სიტყვა '{search_word}' მდებარეობს პოზიციაზე: {pos}")
else:
    print("word not found")