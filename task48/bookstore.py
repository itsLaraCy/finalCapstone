import sqlite3
# Create a connection to the SQLite database
conn = sqlite3.connect('ebookstore.db')

# Create a cursor object
cursor = conn.cursor()

# Create the books table
cursor.execute('''  CREATE TABLE IF NOT EXISTS books
                (id INT PRIMARY KEY NOT NULL,
                Title TEXT NOT NULL,
                Author TEXT NOT NULL,
                Qty INT NOT NULL);''')

# Insert some sample data into the table
cursor.execute("INSERT INTO books (id, Title, Author, Qty) VALUES (3001, 'A Tale of Two Cities', 'Charles Dickens', 30)")
cursor.execute("INSERT INTO books (id, Title, Author, Qty) VALUES (3002, 'Harry Potter and the Philosopher''s Stone', 'J.K. Rowling', 40)")
cursor.execute("INSERT INTO books (id, Title, Author, Qty) VALUES (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25)")
cursor.execute("INSERT INTO books (id, Title, Author, Qty) VALUES (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37)")
cursor.execute("INSERT INTO books (id, Title, Author, Qty) VALUES (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)")


def add_book():
    id = int(input("Enter book id: "))
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = int(input("Enter book quantity: "))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (id, Title, Author, Qty) VALUES (?, ?, ?, ?)", (id, title, author, qty))
    conn.commit()
    cursor.execute("Select * from books")
    print("Book has been entered.")


def update_book():
    id = int(input("Enter book id: "))
    title = input("Enter new book title: ")
    author = input("Enter new book author: ")
    qty = int(input("Enter new book quantity: "))
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET Title = ?, Author = ?, Qty = ? WHERE id = ?", (title, author, qty, id))
    conn.commit()
    print("Book has been updated.")


def delete_book():
    global id
    id = int(input("Enter book id: "))
    cursor.execute("Delete from books WHERE id =?", (id,))


def search_book():
    global id
    id = int(input("Enter book id: "))
    cursor.execute("Select * from books WHERE id =?", (id,))
    details = cursor.fetchall()
    print(details)


# Display menu to the user
while True:
    print("\n1. Enter book\n2. Update book\n3. Delete book\n4. Search books\n0. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 0:
        break
    elif choice == 1:
        # Enter book
        add_book()

    elif choice == 2:
        # Update book
        update_book()

    elif choice == 3:
        # Delete book
        delete_book()


    elif choice == 4:
         search_book()

conn.close()

