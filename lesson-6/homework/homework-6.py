
1)
 vowels = 'aeiouAEIOU'
 result = []
 count = 0
for i in range(len(txt)):
        result.append(txt[i])
if (count + 1) % 3 == 0 and txt[i] not in vowels and (i == 0 or txt[i-1] != '_'):
result.append('_')
count += 1
print(modify_string("hello"))
print(modify_string("assalom"))  
print(modify_string("abcabcabcdeabcdefabcdefg")) 
2)
n = int(input()) 
for i in range(n):
    print(i**2)

3) 
    1) i = 1
while i <= 10:
    print(i)
    i += 1
      2)

     3)num = int(input("Enter number: "))
total = sum(range(1, num+1))
print("Sum is:", total)
      4)num = int(input())  
for i in range(1, 11):
    print(num * i)
     5)numbers = [12, 75, 150, 180, 145, 525, 50]
for number in numbers:
    if number % 25 == 0:
        print(number)
      6)num = int(input(747444)) 
print(len(str((num)))  
      7)

        8)list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)
      9) for i in range(-10, 0):
    print(i)
        10)for i in range(5):
    print(i)
print("Done!")

       11)

4)  def uncommon_elements(list1, list2):
   
    return list(set(list1) ^ set(list2))  

print(uncommon_elements([1, 1, 2], [2, 3, 4])) 
print(uncommon_elements([1, 2, 3], [4, 5, 6])) 
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5])) 





 
