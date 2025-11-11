# PART 3
def distribute_tasks(assignments):
    """
    Divides tasks across days based on their start and due dates,
    balancing the time and difficulty levels evenly.
    """
    distributed_plan = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}
    
    for task_name, subtasks in assignments.items():
        for sub in subtasks:
            subtask_name, total_time, start_day, end_day = sub
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
                    "difficulty": "medium"
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
                print(f"  - {t['task']} → {t['time']} hours (difficulty: {t['difficulty']})")

final_plan = distribute_tasks(assignments)
display_schedule(final_plan)