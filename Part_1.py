print("Welcome to the work planner! Please log your work down below.")

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

assignments_time = {}

for day in week:

    time = input(f"How much time your task it take?(in minutes) on {day}: ")
    
    assignments_time[f"{day}"] = time

print(assignments_time)
