def main():
    print("Welcome to the Stage Calculator")

    # Defined stages data
    stages = {
        "1": {"points": 35, "days": 5},
        "2": {"points": 180, "days": 14},
        "3": {"points": 240, "days": 25},
        "4": {"points": 300, "days": 30}
    }
    
    # 1. Ask for stage
    stage_input = input("What stage are you in? (1-4): ")

    if stage_input not in stages:
        print("Invalid stage selected. Please choose 1, 2, 3, or 4.")
        return

    stage_data = stages[stage_input]
    points_needed = stage_data["points"]
    days_needed = stage_data["days"]

    print(f"For Stage {stage_input}, you need {points_needed} points over {days_needed} days.")

    # 3. Ask for current points
    try:
        current_points = float(input("Enter points you have: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # 4. Calculate status
    if current_points >= points_needed:
        print("Congratulations! You have enough points.")
    else:
        remaining = points_needed - current_points
        print(f"You need {remaining} more points to pass Stage {stage_input}.")
        
        # 5. Calculate daily points needed
        try:
            days_left = int(input("How many days do you have left? "))
            if days_left > 0:
                daily_points = remaining / days_left
                print(f"You need to earn {daily_points:.2f} points per day.")
            else:
                print("You need to get all points today!")
        except ValueError:
            print("Invalid input for days. showing remaining points only.")

if __name__ == "__main__":
    main()
