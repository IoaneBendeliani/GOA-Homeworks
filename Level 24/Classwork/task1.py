"""შექმენით სია რომელშიც ჩამოწერეთ თქვენთვის სასურველი ელემენტები, მინიმუმ 10

indexing
გამოიტანეთ სიაში არსებული მესამე ელემენტი
ჩაანაცვლეთ სიაში არსებული პირველი ელემენტი
slicing
დაბეჭდეთ 2-დან მე-5 ელემენტამდე
დაბეჭდეთ მეორე ელემენტიდან ყველა ელემენტი
დაბეჭდეთ მეხუთე ელემენტამდე ყვეალფერი
დაბეჭდეთ სია შემობრუნებულად"""

martial_arts=["Judo","karate","BJJ","Taekwondo","Muay Thai","Boxing","KickBoxing","Kendo","Sambo","Sumo"]

print(martial_arts[2])
martial_arts[0]="Aikido"

print(martial_arts[1:4])
print(martial_arts[1:])
print(martial_arts[:4])
print(martial_arts[::-1])
