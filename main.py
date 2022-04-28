import syndb

db = syndb.load("test.json", False) ## If not set to True, the database will not be dumped automatically.

def main():
    while True:
        print("""
        1. Set
        2. Get
        3. Delete
        4. Reset
        5. Dump
        6. Load all
        7. Exit
        """)
        choice = input("Enter Choice: ")
        if choice == "1":
            key = input("Enter Key: ")
            value = input("Enter Value: ")
            db.set(key , value)
        elif choice == "2":
            key = input("Enter Key: ")
            db.get(key)
        elif choice == "3":
            key = input("Enter Key: ")
            db.delete(key)
        elif choice == "4":
            db.resetdb()
        elif choice == "5":
            db.dump()
        elif choice == "6":
            db.loadall()
        elif choice == "7":
            exit()
        else:
            print("Invalid Choice")

main()