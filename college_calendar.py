college_calendar = {}

def add_event():
    date = input("Enter date (YYYY-MM-DD): ")
    event = input("Enter event title: ")
    if date in college_calendar:
        college_calendar[date].append(event)
    else:
        college_calendar[date] = [event]
    print("Event added successfully!\n")

def view_events_on_date():
    date = input("Enter date to view events (YYYY-MM-DD): ")
    if date in college_calendar:
        print(f"\nEvents on {date}:")
        for i, event in enumerate(college_calendar[date], 1):
            print(f"{i}. {event}")
    else:
        print("No events found on this date.\n")

def view_all_events():
    if not college_calendar:
        print("No events added yet.")
        return

    print("\n--- College Event Calendar ---")
    for date in sorted(college_calendar):
        print(f"\n{date}:")
        for i, event in enumerate(college_calendar[date], 1):
            print(f"  {i}. {event}")

def main():
    while True:
        print("\n--- College Calendar Menu ---")
        print("1. Add Event")
        print("2. View Events on a Date")
        print("3. View All Events")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_event()
        elif choice == "2":
            view_events_on_date()
        elif choice == "3":
            view_all_events()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()