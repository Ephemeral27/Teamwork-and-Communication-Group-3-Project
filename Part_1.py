print("Welcome to the work planner! Please log your work down below.")
def takes_input():
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    assignments = []
    for day in week:
        daily_task = input(f"What do you have to do for {day}:")
        time = input("How much time will it take?(in minutes)")
        assignments.append([day, daily_task, time])
    return assignments
print(takes_input())

