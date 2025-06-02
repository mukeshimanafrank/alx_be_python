# daily_reminder.py

task = input("Task: ")
priority = input("Priority (low, medium, high): ").lower()
time_bound = input("Time Bound (yes/no): ").lower()

# Match case based on priority
match priority:
    case "high":
        urgency = "Immediate action required!"
    case "medium":
        urgency = "Handle this soon."
    case "low":
        urgency = "No rush, but don't forget."
    case _:
        urgency = "Unknown priority level."

# Modify urgency if task is time-bound
if time_bound == "yes":
    urgency += " This task is time-sensitive!"

# Provide customized reminder
print(f"Reminder: {task} - Priority: {priority.capitalize()}. {urgency}")
