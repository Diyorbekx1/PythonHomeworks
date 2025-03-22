1)
if not isinstance(year, int):
        raise ValueError("Yil butun son bo'lishi kerak.")
    
    print(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

2)
if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")

3)
if a > b:
        a, b = b, a 
even_numbers = []
    for num in range(a, b + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    print(even_numbers)
