# USER GUIDE: Welcome to our study planner! While it is very easy to use, user's should make sure to read the prompts carefully to avoid 
#getting an inaccurate study plan. The information you will be asked to input are:
#the number of assignments you have, whether it has subtasks. For example, if your task is to write a five 
#page essay, you can divide it up into 5 subtasks, each paragraph being 1 subtask}.  
#you will then be asked to provide the name of each subtask, its time duration, and its start and end dates. 
#If the assignment has no subtasks, then you will be asked for the name, time duration, and start and end dates for the assignment or task.


print("Welcome to the work planner! Please log your work down below.")
# Welcomes user to the planner
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Stores day values in a list variable called week
assignments_time = {}
# An empty dictionary variable for assignment time
for day in week:
    time = input(f"How much time do you have to work(in hours) on {day}: ")
# Loops through each value of the week and asks for user input for time
    assignments_time[f"{day}"] = time
# appends the day as the key and the time as the value
print(assignments_time)
# prints the week days and the associated times inputted by the user, all stored in a dictionary.

# part 2
assignments = {}
number_of_assignments = int(input("Please enter how many assignments you have due this week: "))
for i in range(number_of_assignments):
    assignment_name = input("Please enter the assignment name: ")
    #each assignments key is assigned to 0. You need to replace it with the subtasks
    assignments[assignment_name] = 0
    are_there_substasks = input("Does this tasks have subtasks? Enter 'Y' for yes, and 'N' for no: ")
    if are_there_substasks == 'Y':
        how_many_subtasks = int(input("Please enter how many subtasks there are. Please enter a numeric value: "))
        list_of_the_assignment_subtasks = [] # holds all of the subtasks
        for subtask in range(how_many_subtasks): # check what is wrong
            subtask_name = input("Please enter the subtask's name: ")
            subtask = {} # holds the name as key and the time it takes, start and end days as values in a list
            subtask_list = [] # holds the values
            #list_of_the_assignment_subtasks = [] # holds all of the subtasks
            subtask_time_to_complete = int(input("How many hours will this subtasks take? Please enter a numberic value: "))
            subtask_start_day = int(input("Enter the start day for this task. Enter 1 for Monday,2 for Tuesday,3 for Wednesday,4 for Thursday, 5 for Friday, 6 for Saturday, or 7 for Sunday: "))
            subtask_END_day = int(input("Enter the DUE day for this task. Enter 1 for Monday,2 for Tuesday,3 for Wednesday,4 for Thursday, 5 for Friday, 6 for Saturday, or 7 for Sunday: "))
            subtask_list.append(subtask_time_to_complete)
            subtask_list.append(subtask_start_day)
            subtask_list.append(subtask_END_day)
            subtask[subtask_name] = subtask_list
            list_of_the_assignment_subtasks.append(subtask)
        assignments[assignment_name] = list_of_the_assignment_subtasks

    else:
        task_name= assignment_name
        task_name = []
        task_time_to_complete = int(input("How long will this task take? Please enter a numberic value: "))
        task_start_day = int(input("Enter the start day for this task. Enter 1 for Monday,2 for Tuesday,3 for Wednesday,4 for Thursday, 5 for Friday, 6 for Saturday, or 7 for Sunday: "))
        task_END_day = int(input("Enter the DUE day for this task. Enter 1 for Monday,2 for Tuesday,3 for Wednesday,4 for Thursday, 5 for Friday, 6 for Saturday, or 7 for Sunday: "))
        task_name.append(task_time_to_complete)
        task_name.append(task_start_day)
        task_name.append(task_END_day)
        assignments[assignment_name] = task_name
print(assignments) # this is just to show you the nesting of the assignmens and tasks
   
# PART 3
def distribute_tasks(assignments):
    """
    Divides tasks across days based on their start and due dates,
    balancing the time and difficulty levels evenly.
    """
    distributed_plan = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}
    
    for task_name, subtasks in assignments.items():
        # Debugging add case for when assignment has subtasks (list of dict)
        if isinstance(subtasks, list) and all(isinstance(s,dict) for s in subtasks):
            for sub in subtasks:
                for subtask_name, values in sub.items():
                    total_time, start_day, end_day = values
                    num_days = end_day - start_day + 1
                    if num_days <= 0:
                        num_days = 1  # prevent division error
                    time_per_day = round(total_time / num_days, 2)

                    # distribute evenly across the days
                    for d in range(start_day, end_day + 1):
                        day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][d - 1]
                        distributed_plan[day_name].append({
                            "task": f"{task_name} - {subtask_name}",
                            "time": time_per_day,
                            #"difficulty": "medium"
                        })
        
        elif isinstance(subtasks, list) and len(subtasks) == 3:
            #for sub in subtasks:
                    total_time, start_day, end_day = subtasks
                    num_days = end_day - start_day + 1
                    if num_days <= 0:
                        num_days = 1  # prevent division error
                    time_per_day = round(total_time / num_days, 2)

                    # distribute evenly across the days
                    for d in range(start_day, end_day + 1):
                        day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][d - 1]
                        distributed_plan[day_name].append({
                            "task": task_name,
                            "time": time_per_day,
                            #"difficulty": "medium"
                        })
    
    return distributed_plan

#PART 4:
def display_schedule(distributed_plan):
    """
    Prints out tasks in a clear, day-by-day format.
    """
    print("\n===== WEEKLY STUDY PLAN =====")
    for day, tasks in distributed_plan.items():
        print(f"\n{day}:")
        if not tasks:
            print("  (No tasks)")
        else:
            for t in tasks:
                print (f"  - {t['task']} → {t['time']} hours")
                #print(f"  - {t['task']} → {t['time']} hours (difficulty: {t['difficulty']})")

final_plan = distribute_tasks(assignments)
display_schedule(final_plan)
