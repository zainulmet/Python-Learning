class PasswordManager:
    def __init__(self):
        self.passwords = {}
    
    def add_password(self, account, password):
        self.passwords[account] = password
    
    def view_password(self, account):
        if account in self.passwords:
            return self.passwords[account]
        else:
            return None
    
    def update_password(self, account, new_password):
        if account in self.passwords:
            self.passwords[account] = new_password
            print(f"Password for {account} updated.")
        else:
            print(f"{account} not found.")
    
    def delete_password(self, account):
        if account in self.passwords:
            del self.passwords[account]
            print(f"Password for {account} deleted.")
        else:
            print(f"{account} not found.")

# Create a password manager
password_manager = PasswordManager()

print("Welcome to the Password Manager!")

while True:
    print("\nMenu:")
    print("1. Add Password")
    print("2. View Password")
    print("3. Update Password")
    print("4. Delete Password")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        account = input("Enter the account name: ")
        password = input("Enter the password: ")
        password_manager.add_password(account, password)
        print("Password added.")
    elif choice == '2':
        account = input("Enter the account name: ")
        password = password_manager.view_password(account)
        if password:
            print(f"Password for {account}: {password}")
        else:
            print(f"{account} not found.")
    elif choice == '3':
        account = input("Enter the account name: ")
        new_password = input("Enter the new password: ")
        password_manager.update_password(account, new_password)
    elif choice == '4':
        account = input("Enter the account name: ")
        password_manager.delete_password(account)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
