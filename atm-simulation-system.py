# ------------------------------
# ATM Simulation - Python Only 🏦
# ------------------------------

# Initial user data
username = "lalsa"
pin = "1234"
balance = 10000

# Login system
print("===== Welcome to Python ATM =====")
input_username = input("Enter your username: ")
input_pin = input("Enter your 4-digit PIN: ")

if input_username == username and input_pin == pin:
    print("\n✅ Login successful!")

    while True:
        print("\n------- ATM Main Menu -------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            print(f"💰 Your current balance is: ₹{balance}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                balance += amount
                print(f"✅ ₹{amount} deposited successfully.")
                print(f"💰 Updated balance: ₹{balance}")
            else:
                print("❌ Invalid deposit amount.")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            if 0 < amount <= balance:
                balance -= amount
                print(f"✅ ₹{amount} withdrawn successfully.")
                print(f"💰 Remaining balance: ₹{balance}")
            else:
                print("❌ Insufficient balance or invalid amount.")

        elif choice == "4":
            print("🚪 Thank you for using Python ATM. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please select 1, 2, 3, or 4.")

else:
    print("❌ Invalid username or PIN.") 