import json
from datetime import date
# Load the data file

def main_menu():
    while True:
        print("=== Swim Tracker ===")
        print("1. Log a workout")
        print("2. View total yards ")
        print("3. View history")
        print("4. Quit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            log_workout()
        elif choice == 2:
            view_totals()

        elif choice == 3:
            view_history()

        elif choice == 4:
            print("You have ended the SWIM TRACKER")
            quit()




def load_data():
    with open("data.json", "r") as f:
        return json.load(f)

def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f)

def log_workout():
    today = str(date.today())

    warm_up_desc = input("What did you do in warm up (e.g 4x200 freestyle): ")
    warm_up_yards = int(input("Enter the amount of yards in warm up: "))

    pre_set_desc = input("What did you do in the pre set (e.g 3x75 freestyle) if non enter 0: ")
    pre_set_yards = int(input("Enter the amount of yards in the pre set: "))

    main_set_desc = input("What did you do in the main set (e.g 4x200 freestyle 8x50 backstroke): ")
    main_set_yards = int(input("Enter the amount of yards in the main set: "))

    post_set_desc = input("What did you do in the post set (e.g 8x50 backstroke): ")
    post_set_yards = int(input("Enter the amount of yards in the post set: "))

    workout = {
        "date": today,
        "warm_up_desc" : warm_up_desc,
        "warm_up_yards" : warm_up_yards,

        "pre_set_desc" : pre_set_desc,
        "pre_set_yards" : pre_set_yards,

        "main_set_desc" : main_set_desc,
        "main_set_yards" : main_set_yards,

        "post_set_desc" : post_set_desc,
        "post_set_yards" : post_set_yards
    }


    workouts = load_data()
    workouts.append(workout)
    save_data(workouts)



def view_totals():
    workouts = load_data()
    total = 0

    for workout in workouts:
        total += workout["warm_up_yards"] + workout["pre_set_yards"] + workout["main_set_yards"] + workout["post_set_yards"]
    print(f"Total yards: {total}")

def view_history():
    workouts = load_data()

    for workout in workouts:
        print(f"Date: {workout['date']}")
        print(f"Warm up: {workout['warm_up_desc']}")
        print(f"Pre set: {workout['pre_set_desc']}")
        print(f"Main set: {workout['main_set_desc']}")
        print(f"Post set: {workout['post_set_desc']}")
        print()



def main():
    main_menu()

main()