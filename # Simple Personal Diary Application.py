# Simple Personal Diary Application
import datetime

# Diary storage
diary_entries = []

def show_menu():
    print("\n" + "="*40)
    print("        MY PERSONAL DIARY")
    print("="*40)
    print("1. Write New Entry")
    print("2. Read Old Entries") 
    print("3. Exit")
    print("="*40)

def add_entry():
    print("\n--- Write Your Diary Entry ---")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = input("Write your thoughts: ")
    
    diary_entries.append({"date": date, "content": entry})
    print("✓ Entry saved successfully!")
    
    # Save to file
    with open("diary.txt", "a") as file:
        file.write(f"Date: {date}\n")
        file.write(f"Entry: {entry}\n")
        file.write("-" * 30 + "\n")

def read_entries():
    print("\n--- Your Diary Entries ---")
    
    if len(diary_entries) == 0:
        print("No entries yet. Start writing!")
        return
    
    for i, entry in enumerate(diary_entries, 1):
        print(f"\nEntry #{i}")
        print(f"Date: {entry['date']}")
        print(f"Thoughts: {entry['content']}")
        print("-" * 20)

# Load old entries from file
try:
    with open("diary.txt", "r") as file:
        print("Loaded previous entries...")
except:
    print("Starting fresh diary...")

# Main program
print("Welcome to Your Personal Diary!")
print("This is your private space for thoughts :)")

while True:
    show_menu()
    choice = input("Choose option (1-3): ")
    
    if choice == "1":
        add_entry()
    elif choice == "2":
        read_entries()
    elif choice == "3":
        print("Thank you for using your diary! Goodbye!")
        break
    else:
        print("Please choose 1, 2, or 3!")