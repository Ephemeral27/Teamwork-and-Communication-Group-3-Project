print("Welcome to the work planner! Please log your work down below.")

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

assignments = []

for day in week:

    time = input(f"How much time your task it take?(in minutes) on {day}: ")
    

    assignments.append([day, time])

print(assignments)
