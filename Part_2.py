weekly_tasks = []
assignments = {}
number_of_assignments = int(input("Please neter how many assignments you have due this week: "))
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
print(assignments)




