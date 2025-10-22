print("Welcome to the work planner! Please log your work down below.")
# Welcomes user to the planner
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Stores day values in a list variable called week
assignments_time = {}
# An empty dictionary variable for assignment time
for day in week:
    time = input(f"How much time your task it take?(in minutes) on {day}: ")
# Loops through each value of the week and asks for user input for time
    assignments_time[f"{day}"] = time
# appends the day as the key and the time as the value
print(assignments_time)
# prints the week days and the associated times inputted by the user, all stored in a dictionary.