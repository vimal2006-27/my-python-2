from pymysql import *
class pdcode:

    def __init__(self):

        self.con = connect(
            host="localhost",
            user="root",
            password="vimha28",
            database="products"
        )

    def adminreg(self, username, password, email):

        q = """
        INSERT INTO admin(username, password, email)
        VALUES(%s, %s, %s)
        """

        cur = self.con.cursor()
        cur.execute(q, (username, password, email))
        self.con.commit()

        print("Admin registered successfully.")

    def viewadmin(self):

        q = "SELECT * FROM admin"

        cur = self.con.cursor()
        cur.execute(q)

        data = cur.fetchall()

        if data:
            print("\n===== ADMIN DETAILS =====")

            for row in data:
                print(row)
        else:
            print("No admin records found.")

    def adminlogin(self, username, password):

        q = """
        SELECT * FROM admin
        WHERE username=%s AND password=%s
        """

        cur = self.con.cursor()
        cur.execute(q, (username, password))

        data = cur.fetchone()

        if data:
            print("Admin Login Successful.")
            return data[0]
        else:
            print("Invalid username or password.")
            return None

    def change_admin_password(
            self,
            admin_id,
            currentpassword,
            new_password):

        q = """
        SELECT * FROM admin
        WHERE admin_id=%s AND password=%s
        """

        cur = self.con.cursor()
        cur.execute(q, (admin_id, currentpassword))

        data = cur.fetchone()

        if data:

            q = """
            UPDATE admin
            SET password=%s
            WHERE admin_id=%s
            """

            cur.execute(q, (new_password, admin_id))
            self.con.commit()

            print("Password changed successfully.")

        else:
            print("Current password is incorrect.")

    def updateadminprofile(
            self,
            admin_id,
            username,
            email):

        q = """
        UPDATE admin
        SET username=%s, email=%s
        WHERE admin_id=%s
        """

        cur = self.con.cursor()
        cur.execute(q, (username, email, admin_id))

        self.con.commit()

        print("Admin profile updated successfully.")

    def deleteadmin(self, admin_id):

        q = """
        DELETE FROM admin
        WHERE admin_id=%s
        """

        cur = self.con.cursor()
        cur.execute(q, (admin_id,))

        self.con.commit()

        print("Admin deleted successfully.")

    def user(self):

        print("User module.")

    def userreg(
            self,
            username,
            password,
            phone,
            email,
            address,
            dob):

        q = """
        INSERT INTO users
        (username, password, phone, email, address, dob)
        VALUES(%s, %s, %s, %s, %s, %s)
        """

        cur = self.con.cursor()
        cur.execute(
            q,
            (
                username,
                password,
                phone,
                email,
                address,
                dob
            )
        )

        self.con.commit()

        print("User registered successfully.")

    def viewusers(self):

        q = "SELECT * FROM users"

        cur = self.con.cursor()
        cur.execute(q)

        data = cur.fetchall()

        if data:

            print("\n===== USER DETAILS =====")

            for row in data:
                print(row)

        else:
            print("No users found.")

    def userlogin(self, username, password):

        q = """
        SELECT * FROM users
        WHERE username=%s AND password=%s
        """

        cur = self.con.cursor()
        cur.execute(q, (username, password))

        data = cur.fetchone()

        if data:
            print("User Login Successful.")
            return data[0]

        else:
            print("Invalid username or password.")
            return None

    def change_user_password(
            self,
            user_id,
            currentpassword,
            new_password):

        q = """
        SELECT * FROM users
        WHERE user_id=%s AND password=%s
        """

        cur = self.con.cursor()
        cur.execute(q, (user_id, currentpassword))

        data = cur.fetchone()

        if data:

            q = """
            UPDATE users
            SET password=%s
            WHERE user_id=%s
            """

            cur.execute(q, (new_password, user_id))
            self.con.commit()

            print("Password changed successfully.")

        else:
            print("Current password is incorrect.")

    def updateuserprofile(
            self,
            user_id,
            username,
            email,
            phone,
            address,
            dob):

        q = """
        UPDATE users
        SET username=%s,
            email=%s,
            phone=%s,
            address=%s,
            dob=%s
        WHERE user_id=%s
        """

        cur = self.con.cursor()

        cur.execute(
            q,
            (
                username,
                email,
                phone,
                address,
                dob,
                user_id
            )
        )

        self.con.commit()

        print("User profile updated successfully.")

    def supreg(
            self,
            supname,
            comname,
            uname,
            pasw,
            phone,
            email,
            address):

        q = """
        INSERT INTO suppliers
        (
            supplier_name,
            company_name,
            username,
            password,
            phone,
            email,
            address
        )
        VALUES(%s,%s,%s,%s,%s,%s,%s)
        """

        cur = self.con.cursor()

        cur.execute(
            q,
            (
                supname,
                comname,
                uname,
                pasw,
                phone,
                email,
                address
            )
        )

        self.con.commit()

        print("Supplier registered successfully.")

    def suplogin(self, username, password):

        q = """
        SELECT * FROM suppliers
        WHERE username=%s AND password=%s
        """

        cur = self.con.cursor()

        cur.execute(
            q,
            (username, password)
        )

        data = cur.fetchone()

        if data:

            print("Supplier Login Successful.")

            return data[0]

        else:

            print("Invalid username or password.")

            return None


    def viewsup(self):

        q = "SELECT * FROM suppliers"

        cur = self.con.cursor()
        cur.execute(q)

        data = cur.fetchall()

        if data:

            print("\n===== SUPPLIER DETAILS =====")

            for row in data:
                print(row)

        else:

            print("No supplier records found.")

    def change_supplier_password(
            self,
            supplier_id,
            currentpassword,
            new_password):

        q = """
        SELECT * FROM suppliers
        WHERE supplier_id=%s AND password=%s
        """

        cur = self.con.cursor()

        cur.execute(
            q,
            (
                supplier_id,
                currentpassword
            )
        )

        data = cur.fetchone()

        if data:

            q = """
            UPDATE suppliers
            SET password=%s
            WHERE supplier_id=%s
            """

            cur.execute(
                q,
                (
                    new_password,
                    supplier_id
                )
            )

            self.con.commit()

            print("Supplier password changed successfully.")

        else:

            print("Current password is incorrect.")

    def updatsupprofile(
            self,
            supplier_id,
            supname,
            comname,
            uname,
            phone,
            email,
            address):

        q = """
        UPDATE suppliers
        SET supplier_name=%s,
            company_name=%s,
            username=%s,
            phone=%s,
            email=%s,
            address=%s
        WHERE supplier_id=%s
        """

        cur = self.con.cursor()

        cur.execute(
            q,
            (
                supname,
                comname,
                uname,
                phone,
                email,
                address,
                supplier_id
            )
        )

        self.con.commit()

        print("Supplier profile updated successfully.")

    def product(self):

        print("Product module.")


    def add(
            self,
            name,
            cat,
            pur,
            sell,
            qua,
            min_stok):

        q = """
        INSERT INTO products
        (
            ProductName,
            Category,
            PurchasePrice,
            SellingPrice,
            Quantity,
            MinimumStock
        )
        VALUES(%s,%s,%s,%s,%s,%s)
        """

        cur = self.con.cursor()

        cur.execute(
            q,
            (
                name,
                cat,
                pur,
                sell,
                qua,
                min_stok
            )
        )

        self.con.commit()

        print("Product added successfully.")

    def view(self):

        q = "SELECT * FROM products"

        cur = self.con.cursor()
        cur.execute(q)

        data = cur.fetchall()

        if data:

            print("\n===== PRODUCT DETAILS =====")

            for row in data:
                print(row)

        else:

            print("No products found.")

    def search(self,name):

        q = """
        SELECT * FROM products
        WHERE ProductName=%s
        """

        cur = self.con.cursor()

        cur.execute(
            q,
            (name)
        )

        data = cur.fetchone()

        if data:

            print("\nProduct Found:")
            print(data)

        else:

            print("Product not found.")

    def update(
            self,
            id,
            name,
            cat,
            pur,
            sell,
            qua,
            min_stok):

        q = """
        UPDATE products
        SET ProductName=%s,
            Category=%s,
            PurchasePrice=%s,
            SellingPrice=%s,
            Quantity=%s,
            MinimumStock=%s
        WHERE ProductID=%s
        """

        cur = self.con.cursor()

        cur.execute(
            q,
            (
                name,
                cat,
                pur,
                sell,
                qua,
                min_stok,
                id
            )
        )

        self.con.commit()

        if cur.rowcount > 0:

            print("Product updated successfully.")

        else:

            print("Product ID not found.")

    def delete(self, id):

        q = """
        DELETE FROM products
        WHERE ProductID=%s
        """

        cur = self.con.cursor()

        cur.execute(
            q,
            (id,)
        )

        self.con.commit()

        if cur.rowcount > 0:

            print("Product deleted successfully.")

        else:

            print("Product ID not found.")

    def suppllier(self):

        print("Supplier Management Module.")
    def add_supplier(
            self,
            SupplierName,
            Contact,
            Email,
            Address):

        q = """
        INSERT INTO Suppliers
        (
            SupplierName,
            Contact,
            Email,
            Address
        )
        VALUES(%s,%s,%s,%s)
        """

        cur = self.con.cursor()

        cur.execute(
            q,
            (
                SupplierName,
                Contact,
                Email,
                Address
            )
        )

        self.con.commit()

        print("Supplier added successfully.")

    def view_suppliers(self):

        q = "SELECT * FROM Suppliers"

        cur = self.con.cursor()

        cur.execute(q)

        data = cur.fetchall()

        if data:

            print("\n===== SUPPLIER LIST =====")

            for row in data:
                print(row)

        else:

            print("No suppliers found.")

    def Exit(self):

        self.con.close()

        print("Database connection closed.")