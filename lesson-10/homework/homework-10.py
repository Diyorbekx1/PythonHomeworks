1)
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = " Done" if self.completed else " complete"
        return f"Title: {self.title}\nDescription: {self.description}\nDue: {self.due_date}\nStatus: {status}\n"
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        for task in self.tasks:
            print(task)

    def list_incomplete_tasks(self):
        found = False
        for task in self.tasks:
            if not task.completed:
                print(task)
                found = True
        if not found:
            print("All tasks are complete!")

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_complete()
                print(f"Task '{title}' marked as complete!")
                return
        print(f"Task '{title}' not found.")
def main():
    todo = ToDoList()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. List All Tasks")
        print("3. List Incomplete Tasks")
        print("4. Mark Task as Complete")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            task = Task(title, description, due_date)
            todo.add_task(task)
            print("Task added!")

        elif choice == '2':
            print("\n--- All Tasks ---")
            todo.list_all_tasks()

        elif choice == '3':
            print("\n--- Incomplete Tasks ---")
            todo.list_incomplete_tasks()

        elif choice == '4':
            title = input("Enter the title of the task to mark as complete: ")
            todo.mark_task_complete(title)

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")
if __name__ == "__main__":
    main()
2) 
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_title, new_content):
        self.title = new_title
        self.content = new_content

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n"
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        if not self.posts:
            print("No posts found.")
        else:
            for post in self.posts:
                print(post)

    def list_posts_by_author(self, author):
        found = False
        for post in self.posts:
            if post.author.lower() == author.lower():
                print(post)
                found = True
        if not found:
            print(f"No posts found by author: {author}")

    def delete_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                print(f"Post '{title}' deleted.")
                return
        print(f"Post '{title}' not found.")

    def edit_post(self, title, new_title, new_content):
        for post in self.posts:
            if post.title.lower() == title.lower():
                post.edit(new_title, new_content)
                print(f"Post '{title}' updated.")
                return
        print(f"Post '{title}' not found.")

    def latest_posts(self, n=3):
        print(f"--- Latest {n} Posts ---")
        for post in self.posts[-n:][::-1]:
            print(post)
def main():
    blog = Blog()

    while True:
        print("\n--- Simple Blog Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete a Post")
        print("5. Edit a Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("Choose an option (1–7): ")

        if choice == '1':
            title = input("Post Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))
            print("Post added successfully.")

        elif choice == '2':
            print("\n--- All Blog Posts ---")
            blog.list_all_posts()

        elif choice == '3':
            author = input("Enter author name: ")
            blog.list_posts_by_author(author)

        elif choice == '4':
            title = input("Enter the title of the post to delete: ")
            blog.delete_post(title)

        elif choice == '5':
            title = input("Enter the title of the post to edit: ")
            new_title = input("New title: ")
            new_content = input("New content: ")
            blog.edit_post(title, new_title, new_content)

        elif choice == '6':
            try:
                n = int(input("How many latest posts to show? (default 3): ") or 3)
            except ValueError:
                n = 3
            blog.latest_posts(n)

        elif choice == '7':
            print("Exiting blog. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()
3)

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def display(self):
        print(f"Account No: {self.account_number}, Name: {self.holder_name}, Balance: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account
        print("Account added successfully.")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)
        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(f"Transferred {amount} from {from_acc} to {to_acc}.")
            else:
                print("Transfer failed: Insufficient balance.")
        else:
            print("Transfer failed: Invalid account number(s).")


def main():
    bank = Bank()

    while True:
        print("\n--- Banking System Menu ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            acc_num = input("Enter account number: ")
            name = input("Enter holder name: ")
            balance = float(input("Enter initial balance: "))
            acc = Account(acc_num, name, balance)
            bank.add_account(acc)

        elif choice == '2':
            acc_num = input("Enter account number: ")
            acc = bank.get_account(acc_num)
            if acc:
                print(f"Balance: {acc.balance}")
            else:
                print("Account not found.")

        elif choice == '3':
            acc_num = input("Enter account number: ")
            acc = bank.get_account(acc_num)
            if acc:
                amount = float(input("Enter amount to deposit: "))
                acc.deposit(amount)
            else:
                print("Account not found.")

        elif choice == '4':
            acc_num = input("Enter account number: ")
            acc = bank.get_account(acc_num)
            if acc:
                amount = float(input("Enter amount to withdraw: "))
                acc.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == '5':
            from_acc = input("From account: ")
            to_acc = input("To account: ")
            amount = float(input("Amount to transfer: "))
            bank.transfer(from_acc, to_acc, amount)

        elif choice == '6':
            acc_num = input("Enter account number: ")
            acc = bank.get_account(acc_num)
            if acc:
                acc.display()
            else:
                print("Account not found.")

        elif choice == '7':
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
