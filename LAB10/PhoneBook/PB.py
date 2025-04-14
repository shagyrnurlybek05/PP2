import psycopg2
import csv

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    database="lab10",
    user="postgres",
    password=""  # если нет пароля — оставь пустым
)
cur = conn.cursor()

# 1. Добавление из консоли
def insert_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Inserted successfully.\n")

# 2. Загрузка из CSV
def insert_from_csv():
    path = input("CSV path: ")
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (row['name'], row['phone']))
    conn.commit()
    print("CSV data inserted.\n")

# 3. Обновление данных
def update_user():
    old_name = input("Name to update: ")
    new_phone = input("New phone: ")
    cur.execute("UPDATE PhoneBook SET phone = %s WHERE name = %s", (new_phone, old_name))
    conn.commit()
    print("Updated.\n")

# 4. Поиск по фильтру
def query_data():
    name = input("Enter name to search: ")
    cur.execute("SELECT * FROM PhoneBook WHERE name = %s", (name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# 5. Удаление пользователя
def delete_user():
    name = input("Enter name to delete: ")
    cur.execute("DELETE FROM PhoneBook WHERE name = %s", (name,))
    conn.commit()
    print("Deleted.\n")

# Меню
def main():
    while True:
        print("\n📞 PhoneBook Menu:")
        print("1. Insert from console")
        print("2. Insert from CSV")
        print("3. Update user")
        print("4. Query user")
        print("5. Delete user")
        print("6. Exit")
        choice = input("Choose option: ")
        if choice == '1':
            insert_console()
        elif choice == '2':
            insert_from_csv()
        elif choice == '3':
            update_user()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_user()
        elif choice == '6':
            break
        else:
            print("Invalid option.")

    cur.close()
    conn.close()

main()
