Exception Handling Exercises
1) try:
    x = int(input("Son kiriting: "))
    print(10 / x)
except ZeroDivisionError:
    print("Nolga bo‘lish mumkin emas!")
2) try:
    num = int(input("Butun son kiriting: "))
except ValueError:
    print("Bu butun son emas!")
3) try:
    with open("file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Fayl topilmadi!")
4) try:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))
    print(a + b)
except ValueError:
    print("Faqat son kiriting!")
5) try:
    with open("/root/protected.txt", "r") as f:
        print(f.read())
except PermissionError:
    print("Faylga ruxsat yo‘q!")
6) my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Index mavjud emas!")
7) try:
    num = int(input("Iltimos, son kiriting: "))
    print(f"Siz {num} sonini kiritdingiz.")
except KeyboardInterrupt:
    print("\nKiritish bekor qilindi! (KeyboardInterrupt)")
8) try:
    a = int(input("Birinchi sonni kiriting: "))
    b = int(input("Ikkinchi sonni kiriting: "))
    result = a / b
    print("Natija:", result)
except ArithmeticError:
    print("Arifmetik xato yuz berdi! Nolga bo‘lish mumkin emas.")
9) try:
    with open("test.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
except UnicodeDecodeError:
    print("Faylni ochishda kodlash xatosi yuz berdi!")
10) try:
    my_list = [1, 2, 3]
    my_list.append(4)
    my_list.push(5)  
except AttributeError:
    print("Xatolik: List bu atribut yoki metodga ega emas!")
  File Input/Output Exercises
1) with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
2) def read_n_lines(filename, n):
    with open(filename, "r") as file:
        for _ in range(n):
            print(file.readline(), end="")

read_n_lines("sample.txt", 3) 
3) with open("sample.txt", "a") as file:
    file.write("Yangi qator qo‘shildi.")

with open("sample.txt", "r") as file:
    print(file.read())
4) def read_last_n_lines(filename, n):
    with open(filename, "r") as file:
        lines = file.readlines()
        print("".join(lines[-n:]))

read_last_n_lines("sample.txt", 3)  
5) with open("sample.txt", "r") as file:
    lines_list = file.readlines()

print(lines_list)
6) with open("sample.txt", "r") as file:
    content = file.read()

print(content)

7) 
with open("sample.txt", "r") as file:
    lines_array = array(file.readlines())

print(lines_array)

8) def find_longest_word(filename):
    with open(filename, "r") as file:
        words = file.read().split()
        longest_word = max(words, key=len)
        return longest_word
print(find_longest_word("sample.txt"))

9) with open("sample.txt", "r") as file:
    line_count = sum(1 for _ in file)

print("Faylda", line_count, "ta qator bor.")
10)

with open("sample.txt", "r") as file:
    words = file.read().split()
    word_freq = Counter(words)

print(word_freq)
11) import os

file_size = os.path.getsize("sample.txt")
print("Fayl hajmi:", file_size, "bayt")
12) my_list = ["Apple", "Banana", "Cherry"]

with open("sample.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")
13) with open("sample.txt", "r") as src, open("copy.txt", "w") as dest:
    dest.write(src.read())

14)
15)
with open("sample.txt", "r") as file:
    lines = file.readlines()

print(random.choice(lines))
16) file = open("sample.txt", "r")
print("Fayl yopiqmi?", file.closed)
file.close()
print("Fayl yopiqmi?", file.closed)
17) with open("sample.txt", "r") as file:
    lines = [line.strip() for line in file]

print(lines)

18) with open("sample.txt", "r") as file:
    words = file.read().len()
    print("So‘zlar soni:", len(words))
19)


