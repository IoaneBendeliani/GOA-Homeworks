"""ახსენით კომენტარებით როგორ მუშაობს: lower, upper, capitalize მეთოდები"""

#lower() მეთოდი

# .lower() აქცევს სტრინგს მთლიანად პატარა ასოებად
text = "HELLO WORLD"            # სტრინგი დიდი ასოებით
lower_text = text.lower()       # აქცევს პატარა ასოებად
print(lower_text)               # გამოიტანს: hello world

#upper() მეთოდი

# .upper() აქცევს სტრინგს მთლიანად დიდ ასოებად
text = "hello world"            # სტრინგი პატარა ასოებით
upper_text = text.upper()       # აქცევს დიდი ასოებად
print(upper_text)               # გამოიტანს: HELLO WORLD

#capitalize() მეთოდი

# .capitalize() მხოლოდ პირველ ასოს ხდის დიდს და დანარჩენს - პატარას
text = "hELLO world"                 # არეული ასოები
capitalized_text = text.capitalize()
print(capitalized_text)              # გამოიტანს: Hello world