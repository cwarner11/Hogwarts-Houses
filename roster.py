import csv
import sys
from cs50 import SQL

def main():

    # Checks user input
    if len(sys.argv) != 2:
        print("Error, Try again")
        sys.exit()

    open("students.db", "r").close()
    db = SQL("sqlite:///students.db")

    student = list()
    houses = sys.argv[1]

    student = db.execute("SELECT first,middle,last,birth FROM students WHERE house = ? ORDER BY last,first", houses)

    for row in student:

        print(row["first"], end = ' ')

        if row["middle"] != None:
            print(row["middle"], end = ' ')

        print(row["last"], end = ',')

        print(f" born",row["birth"])

main()
