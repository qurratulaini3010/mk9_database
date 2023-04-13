from flask import Flask
from db import connect_to_database

app = Flask(__name__)

# Establish a connection to the database
mydb = connect_to_database()

# Create a cursor object to execute queries
mycursor = mydb.cursor()


# Define a route to retrieve data from the database
@app.route("/")
def get_data():
    mycursor.execute("SELECT * FROM `mk9-database`")
    data = mycursor.fetchall()
    return str(data)


if __name__ == "__main__":
    app.run()
