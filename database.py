import sqlite3 as sqlite

db = "../users.db"

# Adds a user to the database
def insert(first_name,last_name,email,fav_number):
    # Connect to the database
    conn = sqlite.connect(db)
    # Create the cursor
    c = conn.cursor()
    # Create the table if it doesn't already exist
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        first_name text,
        last_name text,
        email text,
        fav_number integer
    )
    """)
    

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
     # Create the table if it doesn't already exist
    c.execute("""CREATE TABLE IF NOT EXISTS projects (
        first_name text,
        last_name text,
        email text,
        fav_number integer
    )
    """)


    c.execute("SELECT * FROM users WHERE email = (?)",(email,)) # johns@jmail.com

    items = c.fetchall()


    # Commit changes
    conn.commit()
    # Close database
    conn.close()

    try: items[0]
    except IndexError: return 404

    
    return items[0]

    












    

