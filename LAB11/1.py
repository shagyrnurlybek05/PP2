import psycopg2

def connect():
    return psycopg2.connect(
        host="localhost",
        database="Lab11",
        user="postgres",
        password=""
    )

def call_insert_or_update():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
            print("User inserted/updated.")

def call_insert_many():
    names = input("Enter names (comma separated): ").split(',')
    phones = input("Enter phones (comma separated): ").split(',')
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
            print("Users processed.")

def call_find():
    pattern = input("Enter search pattern: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM find_users(%s)", (pattern,))
            for row in cur.fetchall():
                print(row)

def call_paginated():
    lim = int(input("Limit: "))
    off = int(input("Offset: "))
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_users_paginated(%s, %s)", (lim, off))
            for row in cur.fetchall():
                print(row)

def call_delete():
    val = input("Enter name or phone to delete: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_user_by_value(%s)", (val,))
            print("Deleted.")

def main():
    while True:
        print("""
PhoneBook Menu:
1. Insert or Update User
2. Insert Many Users
3. Search by Pattern
4. Paginated Query
5. Delete by Name or Phone
6. Exit
        """)
        choice = input("Choose: ")
        if choice == '1':
            call_insert_or_update()
        elif choice == '2':
            call_insert_many()
        elif choice == '3':
            call_find()
        elif choice == '4':
            call_paginated()
        elif choice == '5':
            call_delete()
        elif choice == '6':
            break

main()
