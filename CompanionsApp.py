import database

MENU_PROMPT = """-- Doctor Who Companion App --

Please choose one of these options:

1) Add a new companion
2) See all companions
3) Find a companion by name
4) See the best adventure for a companion
5) Delete a companion
6) Exit

Your selection:"""


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "6":
        if user_input == "1":
            prompt_add_new_companion(connection)
        elif user_input == "2":
            prompt_see_all_companions(connection)
        elif user_input == "3":
            prompt_find_companion(connection)
        elif user_input == "4":
            prompt_find_best_adventure(connection)
        elif user_input == "5":
            prompt_delete_companion(connection)
        else:
            print("Invalid input... please try again!")


def prompt_add_new_companion(connection):
    name = input("Enter companion name: ")
    adventure = input("Enter their adventure: ")
    rating = int(input("Rate the adventure (0-100): "))

    database.add_companion(connection, name, adventure, rating)


def prompt_see_all_companions(connection):
    companions = database.get_all_companions(connection)

    for companion in companions:
        print(f"ID: {companion[0]} | {companion[1]} - {companion[2]} ({companion[3]}/100)")


def prompt_find_companion(connection):
    name = input("Enter companion name to find: ")
    companions = database.get_companions_by_name(connection, name)

    for companion in companions:
        print(f"ID: {companion[0]} | {companion[1]} - {companion[2]} ({companion[3]}/100)")


def prompt_find_best_adventure(connection):
    name = input("Enter companion name: ")
    best = database.get_best_adventure_for_companion(connection, name)

    if best:
        print(f"Best adventure for {name}: {best[2]} ({best[3]}/100)")
    else:
        print("No data found.")


def prompt_delete_companion(connection):
    choice = input("Delete by (1) ID or (2) Name? ")

    if choice == "1":
        companion_id = int(input("Enter companion ID to delete: "))
        database.delete_companion_by_id(connection, companion_id)
        print("Companion deleted.")

    elif choice == "2":
        name = input("Enter companion name to delete: ")
        database.delete_companion_by_name(connection, name)
        print("Companion(s) deleted.")

    else:
        print("Invalid choice.")


menu()