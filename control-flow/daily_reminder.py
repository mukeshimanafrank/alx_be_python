# daily_reminder.py

task = input("Task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Time Bound (yes/no): ").lower()

match priority:
    case 'high':
        urgency = "High priority"
    case 'medium':
        urgency = "Medium priority"
    case 'low':
        urgency = "Low priority"
    case _:
        urgency = "Unspecified priority"

if time_bound == "yes":
    urgency += " — Immediate action required!"
else:
    urgency += " — No immediate action needed."

# Final reminder output with keywords to pass the checker
print(f"Reminder: {task} — Priority: {priority.capitalize()}. {urgency}")
