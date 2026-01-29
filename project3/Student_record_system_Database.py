import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school_db"
)
cursor = db.cursor()
def id_exists(sid):
    cursor.execute("SELECT id FROM results WHERE id=%s", (sid,))
    return cursor.fetchone() is not None

def store():
    n = int(input("Enter number of students: "))
    for i in range(1, n + 1):
        print(f"\n----- Student {i} -----")

        sid = int(input("Enter Student ID: "))
        name = input("Name: ")

        p = int(input("Physics: "))
        b = int(input("Biology: "))
        m = int(input("Maths: "))
        c = int(input("Chemistry: "))
        e = int(input("English: "))
        nep = int(input("Nepali: "))

        # simple validation
        if any(x < 0 or x > 75 for x in [p, b, m, c, e, nep]):
            print("Invalid marks! Must be 0-75. Skipping student.")
            continue

        total = p + b + m + c + e + nep
        percentage = (total / 450) * 100

        # pass/fail logic
        if any(x < 35 for x in [p, b, m, c, e, nep]):
            output = "Fail"
            division = "Fail"
        else:
            output = "Pass"
            if percentage >= 80:
                division = "Distinction"
            elif percentage >= 60:
                division = "First Division"
            elif percentage >= 45:
                division = "Second Division"
            else:
                division = "Third Division"

        # if ID exists → update else insert
        if id_exists(sid):
            sql = """UPDATE results SET
                     name=%s, Physics=%s, Bio=%s, Maths=%s, Chemistry=%s,
                     English=%s, Nepali=%s, total=%s, percentage=%s,
                     division=%s, output=%s
                     WHERE id=%s"""
            values = (name, p, b, m, c, e, nep, total, percentage, division, output, sid)
            cursor.execute(sql, values)
            print("Record updated successfully!")
        else:
            sql = """INSERT INTO results
                     (id, name, Physics, Bio, Maths, Chemistry, English, Nepali,
                      total, percentage, division, output)
                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            values = (sid, name, p, b, m, c, e, nep, total, percentage, division, output)
            cursor.execute(sql, values)
            print("Record added successfully!")

        db.commit()

# ---------- VIEW STUDENT ----------
def display_student():
    sid = input("Enter Student ID: ")
    cursor.execute("SELECT * FROM results WHERE id=%s", (sid,))
    r = cursor.fetchone()
    if r:
        print(f"\nID:{r[0]} | Name:{r[1]}")
        print(f"Physics:{r[2]} Bio:{r[3]} Maths:{r[4]}")
        print(f"Chemistry:{r[5]} English:{r[6]} Nepali:{r[7]}")
        print(f"Total:{r[8]} | Percentage:{r[9]:.2f}%")
        print(f"Division:{r[10]} | Result:{r[11]}")
    else:
        print("Student not found!")

# ---------- DELETE STUDENT ----------
def delete_student():
    sid = input("Enter Student ID to delete: ")
    if id_exists(sid):
        cursor.execute("DELETE FROM results WHERE id=%s", (sid,))
        db.commit()
        print("Record deleted successfully!")
    else:
        print("Student ID not found!")

# ---------- PRINT REPORT ----------
def print_report():
    sid = input("Enter Student ID: ")
    cursor.execute("SELECT * FROM results WHERE id=%s", (sid,))
    s = cursor.fetchone()
    if s:
        with open(f"{s[1]}_Report.txt", "w") as f:
            f.write("STUDENT REPORT CARD\n")
            f.write("===================\n")
            f.write(f"ID: {s[0]}\nName: {s[1]}\n")
            f.write(f"Total: {s[8]}\nPercentage: {s[9]:.2f}%\n")
            f.write(f"Division: {s[10]}\nResult: {s[11]}\n")
        print("Report generated successfully!")
    else:
        print("Student not found!")

# ---------- MENU ----------
while True:
    print("\n--- MENU ---")
    print("1. Add / Update Student")
    print("2. View Student")
    print("3. Print Report")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        store()
    elif choice == '2':
        display_student()
    elif choice == '3':
        print_report()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting program...")
        break
