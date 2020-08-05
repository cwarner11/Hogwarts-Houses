import csv
import sys
from cs50 import SQL

def main():

    # Checks user input
    if len(sys.argv) != 2:
        print("Error, Try again")
        sys.exit()

    # Creates database
    open("students.db", "w").close()
    db = SQL("sqlite:///students.db")

    db.execute("CREATE TABLE students(first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERIC)")

    characters = sys.argv[1]

    # Reads csv from argv[1]
    with open(characters, "r") as csv_file:

        # Creates DictReader
        csv_reader = csv.DictReader(csv_file)

        # Loops over each line in DictReader
        for line in csv_reader:

            new_dict = list()
            new_dict.append(line['name'].split())
            last_dict = new_dict[0]

            if len(last_dict) == 2:
                db.execute("INSERT INTO students(first,last,house,birth) VALUES (?,?,?,?)",last_dict[0], last_dict[1], line["house"], int(line["birth"]))

            if len(last_dict) == 3:
                db.execute("INSERT INTO students(first,middle,last,house,birth) VALUES (?,?,?,?,?)",last_dict[0], last_dict[1],last_dict[2], line["house"], int(line["birth"]))




main()
