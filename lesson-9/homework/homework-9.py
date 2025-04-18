1)import math
 
 class Circle:
     def __init__(self, radius):
         self.radius = radius
 
     def area(self):
         return math.pi * self.radius ** 2
 
     def perimeter(self):
         return 2 * math.pi * self.radius
 2)
 from datetime import datetime
 
 class Person:
     def __init__(self, name, country, birth_date):
         self.name = name
         self.country = country
         self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
 
     def age(self):
         today = datetime.today()
         return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
   3)
   class Calculator:
     def add(self, x, y):
         return x + y
 
     def subtract(self, x, y):
         return x - y
 
     def multiply(self, x, y):
         return x * y
 
     def divide(self, x, y):
         if y == 0:
             return "ZeroDivisionError"
         return x / y
 4)
   import math
 
 class Shape:
     def area(self):
         pass
 
     def perimeter(self):
         pass
 
 class Circle(Shape):
     def __init__(self, radius):
         self.radius = radius
 
     def area(self):
         return math.pi * self.radius ** 2
 
     def perimeter(self):
         return 2 * math.pi * self.radius
 
 class Square(Shape):
     def __init__(self, side):
         self.side = side
 
     def area(self):
         return self.side ** 2
 
     def perimeter(self):
         return 4 * self.side
 
 class Triangle(Shape):
     def __init__(self, a, b, c):
         self.a, self.b, self.c = a, b, c
 
     def perimeter(self):
         return self.a + self.b + self.c
 
     def area(self):
         s = self.perimeter() / 2
         return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
 5)
   class Node:
     def __init__(self, value):
         self.value = value
         self.left = None
         self.right = None
 
 class BinarySearchTree:
     def __init__(self):
         self.root = None
 
     def insert(self, value):
         if not self.root:
             self.root = Node(value)
         else:
             self._insert_rec(self.root, value)
 
     def _insert_rec(self, node, value):
         if value < node.value:
             if node.left is None:
                 node.left = Node(value)
             else:
                 self._insert_rec(node.left, value)
         elif value > node.value:
             if node.right is None:
                 node.right = Node(value)
             else:
                 self._insert_rec(node.right, value)
 
     def search(self, value):
         return self._search_rec(self.root, value)
 
     def _search_rec(self, node, value):
         if node is None:
             return False
         if node.value == value:
             return True
         elif value < node.value:
             return self._search_rec(node.left, value)
         else:
             return self._search_rec(node.right, value)
 6)
   class Stack:
     def __init__(self):
         self.items = []
 
     def push(self, item):
         self.items.append(item)
 
     def pop(self):
         if not self.items:
             return "Stack is empty"
         return self.items.pop()
 7)
   class Node:
     def __init__(self, data):
         self.data = data
         self.next = None
 
 class LinkedList:
     def __init__(self):
         self.head = None
 
     def insert(self, data):
         new_node = Node(data)
         if not self.head:
             self.head = new_node
         else:
             curr = self.head
             while curr.next:
                 curr = curr.next
             curr.next = new_node
 
     def delete(self, data):
         curr = self.head
         if curr and curr.data == data:
             self.head = curr.next
             return
         prev = None
         while curr and curr.data != data:
             prev = curr
             curr = curr.next
         if curr:
             prev.next = curr.next
 
     def display(self):
         curr = self.head
         while curr:
             print(curr.data, end=" -> ")
             curr = curr.next
         print("None")
 8)
   class ShoppingCart:
     def __init__(self):
         self.items = {}
 
     def add_item(self, item, price):
         self.items[item] = self.items.get(item, 0) + price
 
     def remove_item(self, item):
         if item in self.items:
             del self.items[item]
 
     def total_price(self):
         return sum(self.items.values())
 9)
   class Stack:
     def __init__(self):
         self.stack = []
 
     def push(self, val):
         self.stack.append(val)
 
     def pop(self):
         if not self.stack:
             return "Stack is empty"
         return self.stack.pop()
 
     def display(self):
         print("Stack elements:", self.stack)
 10)
   class Queue:
     def __init__(self):
         self.queue = []
 
     def enqueue(self, item):
         self.queue.append(item)
 
     def dequeue(self):
         if not self.queue:
             return "Queue is empty"
         return self.queue.pop(0)
 
     def display(self):
         print("Queue:", self.queue)
