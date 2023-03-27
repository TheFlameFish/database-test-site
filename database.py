import sqlite3 as sqlite

db = "users.db"

# Adds a user to the database
def insert(first_name,last_name,email,fav_number):
    # Connect to the database
    conn = sqlite.connect(db)
    # Create the cursor
    c = conn.cursor()
    
    c.execute("INSERT INTO users VALUES (?,?,?,?)", (first_name,last_name,email,fav_number))

    # Commit changes
    conn.commit()
    # Close database
    conn.close()

# Looks up a user by email
def lookup_email(email):
    # Connect to the database
    conn = sqlite.connect(db)

    # Create the cursor
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE email = (?)",(email,)) # johns@jmail.com

    items = c.fetchall()


    # Commit changes
    conn.commit()
    # Close database
    conn.close()

    try: items[0]
    except IndexError: return 404

    
    return items[0]

    












    

