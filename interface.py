import sqlite3 as sqlite
import flask

# Connect to the database
conn = sqlite.connect('users.db')

# Create the cursor
c = conn.cursor()

# Create a table
#c.execute("""CREATE TABLE

#""")