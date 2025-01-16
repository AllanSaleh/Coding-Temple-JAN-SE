name = "Allan"
students = ["Noel", "Cody", "Joseph", "Karla", "Kortney"]

tasks = ["fix bug", "write unit tests", "review code", "update documentation"]
print("first task:", tasks[0])
print("third task:", tasks[2])
print("last task:", tasks[-1])
print(tasks)

# Adding tasks
tasks.append("optimize database query")
tasks.append("refactor code")
print(tasks)

print("*"*30)
tasks.insert(2, "deploy to staging")
print(tasks)

print("*"*30)

# Remove tasks
tasks.remove("write unit tests")
print(tasks)

print("*"*30)

del tasks[3]
print(tasks)

# Removing and retrieving the last task with pop()
print("*"*30)

removed_element = tasks.pop()
print(f"Removed {removed_element} from the tasks list")
print(tasks)

print("*"*30)
tasks.pop(1)
print(tasks)

# Extending the task list with more tasks
more_tasks = ["setup CI/CD", "conduct coding reviews"]
tasks.extend(more_tasks)
print(f"\nExtended tasks list: {tasks}")

# Slicing
first_three_tasks = tasks[0:3]
print(f"\nFirst three tasks: {first_three_tasks}")

last_two_tasks = tasks[:-3]
last_two_tasks2 = tasks[3:]
print(f"\nLast two tasks: {last_two_tasks2}")

second_and_third_tasks = tasks[1:3]
print(f"\nSecond and third tasks: {second_and_third_tasks}")

print("*"*30)

# Nested Lists
tasks.append(["add API endpoint", "fix frontend bug", "update database schema"])
print(tasks)

print("*"*30)
print(f"Last element of tasks: {tasks[-1]}" )

print(f"Second element of inner list: {tasks[-1][1]}")

print(f"First element of inner list: {tasks[-1][0]}")


# print(isinstance(tasks, int))

print("\nLooping through the task list")
for task in tasks:
    print(task)
    


print("\nLooping through every task and subtask")

# for index, task in enumerate(tasks):
#     if isinstance(task, list):
#         for subtask in task:
#             print(subtask)
#     else:
#         print(f"{index + 1}) {task}")
for task in tasks:
    if isinstance(task, list):
        for subtask in task:
            print(subtask)
    else:
        print(f"{task}")

# Clearing the task list
tasks.clear()
print(tasks)

task_duration = [4,1,1.5,2,0.5]
print(f"\nMax task duration: {max(task_duration)}")
print(f"\nMin task duration: {min(task_duration)}")

# Sorting and reversing task duration
task_duration.sort(reverse=True)
print(f"\nSorted task durations: {task_duration}")

task_duration.reverse()
print(f"\nReversed sorted task duration: {task_duration}")