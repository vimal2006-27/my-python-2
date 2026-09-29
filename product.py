from pdcode import pdcode

def admin_menu(db):
    while True:

        print("\n========== ADMIN MENU ==========")

        print("1. Admin Registration")
        print("2. View Admins")
        print("3. Admin Login")
        print("4. Change Password")
        print("5. Update Profile")
        print("6. Delete Admin")
        print("7. Back")

        try:
            c = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a number.")
            continue
        if c == 1:

            username = input("Enter Username: ")
            password = input("Enter Password: ")
            email = input("Enter Email: ")

            db.adminreg(
                username,
                password,
                email
            )
        elif c == 2:

            db.viewadmin()


        elif c == 3:

            username = input("Enter Username: ")
            password = input("Enter Password: ")

            admin_id = db.adminlogin(
                username,
                password
            )

            if admin_id:

                product_menu(db)

        elif c == 4:

            admin_id = int(
                input("Enter Admin ID: ")
            )

            currentpassword = input(
                "Enter Current Password: "
            )

            new_password = input(
                "Enter New Password: "
            )

            db.change_admin_password(
                admin_id,
                currentpassword,
                new_password
            )

        elif c == 5:

            admin_id = int(
                input("Enter Admin ID: ")
            )

            username = input(
                "Enter New Username: "
            )

            email = input(
                "Enter New Email: "
            )

            db.updateadminprofile(
                admin_id,
                username,
                email
            )
        elif c == 6:

            admin_id = int(
                input("Enter Admin ID: ")
            )

            db.deleteadmin(admin_id)

        elif c == 7:

            break

        else:

            print("Invalid choice.")

def user_menu(db):

    while True:

        print("\n========== CUSTOMER MENU ==========")

        print("1. User Registration")
        print("2. View Users")
        print("3. User Login")
        print("4. Change Password")
        print("5. Update Profile")
        print("6. Back")

        try:
            c = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a number.")
            continue

        if c == 1:

            username = input("Enter Username: ")
            password = input("Enter Password: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            dob = input(
                "Enter DOB (YYYY-MM-DD): "
            )

            db.userreg(
                username,
                password,
                phone,
                email,
                address,
                dob
            )
        elif c == 2:

            db.viewusers()

        elif c == 3:

            username = input("Enter Username: ")
            password = input("Enter Password: ")

            user_id = db.userlogin(
                username,
                password
            )

            if user_id:

                customer_product_menu(db)

        elif c == 4:

            user_id = int(
                input("Enter User ID: ")
            )

            currentpassword = input(
                "Enter Current Password: "
            )

            new_password = input(
                "Enter New Password: "
            )

            db.change_user_password(
                user_id,
                currentpassword,
                new_password
            )


        elif c == 5:

            user_id = int(
                input("Enter User ID: ")
            )

            username = input(
                "Enter Username: "
            )

            email = input(
                "Enter Email: "
            )

            phone = input(
                "Enter Phone: "
            )

            address = input(
                "Enter Address: "
            )

            dob = input(
                "Enter DOB (YYYY-MM-DD): "
            )

            db.updateuserprofile(
                user_id,
                username,
                email,
                phone,
                address,
                dob
            )


        elif c == 6:

            break

        else:

            print("Invalid choice.")



def Supplier_menu(db):

    while True:

        print("\n========== SUPPLIER MENU ==========")

        print("1. Supplier Registration")
        print("2. Supplier Login")
        print("3. View Suppliers")
        print("4. Change Password")
        print("5. Update Supplier Profile")
        print("6. Back")

        try:
            c = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a number.")
            continue

        if c == 1:

            supname = input(
                "Enter Supplier Name: "
            )

            comname = input(
                "Enter Company Name: "
            )

            uname = input(
                "Enter Username: "
            )

            pasw = input(
                "Enter Password: "
            )

            phone = input(
                "Enter Phone: "
            )

            email = input(
                "Enter Email: "
            )

            address = input(
                "Enter Address: "
            )

            db.supreg(
                supname,
                comname,
                uname,
                pasw,
                phone,
                email,
                address
            )

        elif c == 2:

            username = input(
                "Enter Username: "
            )

            password = input(
                "Enter Password: "
            )

            supplier_id = db.suplogin(
                username,
                password
            )

            if supplier_id:

                supplier_product_menu(db)

        elif c == 3:

            db.viewsup()

        elif c == 4:

            supplier_id = int(
                input("Enter Supplier ID: ")
            )

            currentpassword = input(
                "Enter Current Password: "
            )

            new_password = input(
                "Enter New Password: "
            )

            db.change_supplier_password(
                supplier_id,
                currentpassword,
                new_password
            )
        elif c == 5:

            supplier_id = int(
                input("Enter Supplier ID: ")
            )

            supname = input(
                "Enter Supplier Name: "
            )

            comname = input(
                "Enter Company Name: "
            )

            uname = input(
                "Enter Username: "
            )

            phone = input(
                "Enter Phone: "
            )

            email = input(
                "Enter Email: "
            )

            address = input(
                "Enter Address: "
            )

            db.updatsupprofile(
                supplier_id,
                supname,
                comname,
                uname,
                phone,
                email,
                address
            )


        elif c == 6:

            break

        else:

            print("Invalid choice.")


def product_menu(db):

    while True:

        print("\n========== PRODUCT MANAGEMENT ==========")

        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Supplier Management")
        print("7. Logout")

        try:
            c = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a number.")
            continue

        if c == 1:

            name = input(
                "Enter Product Name: "
            )

            cat = input(
                "Enter Category: "
            )

            pur = float(
                input("Enter Purchase Price: ")
            )

            sell = float(
                input("Enter Selling Price: ")
            )

            qua = int(
                input("Enter Quantity: ")
            )

            min_stok = int(
                input("Enter Minimum Stock: ")
            )

            db.add(
                name,
                cat,
                pur,
                sell,
                qua,
                min_stok
            )


        elif c == 2:

            db.view()


        elif c == 3:
            name = input(
                "Enter Product Name: "
            )

            db.search(
                name
            )

        elif c == 4:

            id = int(
                input("Enter Product ID: ")
            )

            name = input(
                "Enter Product Name: "
            )

            cat = input(
                "Enter Category: "
            )

            pur = float(
                input("Enter Purchase Price: ")
            )

            sell = float(
                input("Enter Selling Price: ")
            )

            qua = int(
                input("Enter Quantity: ")
            )

            min_stok = int(
                input("Enter Minimum Stock: ")
            )

            db.update(
                id,
                name,
                cat,
                pur,
                sell,
                qua,
                min_stok
            )

        elif c == 5:

            id = int(
                input("Enter Product ID: ")
            )

            db.delete(id)

        elif c == 6:

            supplier_me(db)

        elif c == 7:

            print("Admin Logout.")

            break

        else:

            print("Invalid choice.")

def customer_product_menu(db):

    while True:

        print("\n========== CUSTOMER PRODUCT MENU ==========")

        print("1. View Products")
        print("2. Search Product")
        print("3. Logout")

        try:
            c = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a number.")
            continue

        if c == 1:

            db.view()

        elif c == 2:

            name = input(
                "Enter Product Name: "
            )

            db.search(
                name
            )

        elif c == 3:

            print("Customer Logout.")

            break

        else:

            print("Invalid choice.")

def supplier_product_menu(db):

    while True:

        print("\n========== SUPPLIER PRODUCT MENU ==========")

        print("1. View Products")
        print("2. Search Product")
        print("3. Logout")

        try:
            c = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a number.")
            continue

        if c == 1:

            db.view()

        elif c == 2:
            name = input(
                "Enter Product Name: "
            )

            db.search(
                name
            )

        elif c == 3:

            print("Supplier Logout.")

            break

        else:

            print("Invalid choice.")

def supplier_me(db):

    while True:

        print("\n========== SUPPLIER MANAGEMENT ==========")

        print("1. Add Supplier")
        print("2. View Suppliers")
        print("3. Back")

        try:
            c = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a number.")
            continue

        if c == 1:

            SupplierName = input(
                "Enter Supplier Name: "
            )

            Contact = input(
                "Enter Contact: "
            )

            Email = input(
                "Enter Email: "
            )

            Address = input(
                "Enter Address: "
            )

            db.add_supplier(
                SupplierName,
                Contact,
                Email,
                Address
            )

        elif c == 2:

            db.view_suppliers()
        elif c == 3:

            break

        else:

            print("Invalid choice.")