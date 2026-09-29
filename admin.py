from pdcode import pdcode
from product import (
    admin_menu,
    user_menu,
    Supplier_menu
)
try:
    db = pdcode()

    while True:

        print("\n================================")
        print("     PRODUCT MANAGEMENT SYSTEM")
        print("================================")

        print("1. Admin")
        print("2. Customer")
        print("3. Supplier")
        print("4. Exit")

        try:
            c = int(
                input("Enter your choice: ")
            )

        except ValueError:

            print("Please enter a number.")
            continue
        if c == 1:

            admin_menu(db)

        elif c == 2:

            user_menu(db)

        elif c == 3:

            Supplier_menu(db)

        elif c == 4:

            print("Thank you..!")
            break

        else:

            print("Invalid choice.")


except Exception as e:

    print("Error:", e)