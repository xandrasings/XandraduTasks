import json

from service import todoist_service



habit_task_completions = {}


#deserialize from json file
with open('user_data/habit_tasks_completions.json', 'r') as file:
    habit_task_completions = json.load(file)
for habit_id in habit_task_completions:
    for task_id in habit_task_completions[habit_id]:
        habit_task_completions[habit_id][task_id] = set(habit_task_completions[habit_id][task_id])

for habit_id in habit_task_completions:
    for task_id in habit_task_completions[habit_id]:
        habit_task_completions[habit_id][task_id].update(todoist_service.getTaskCompletions(task_id))


#serialize to json
for habit_id in habit_task_completions:
    for task_id in habit_task_completions[habit_id]:
        habit_task_completions[habit_id][task_id] = list(habit_task_completions[habit_id][task_id])
        habit_task_completions[habit_id][task_id].sort(reverse=True)
jsondata = json.dumps(habit_task_completions, indent=4)

#save to file
with open('user_data/habit_tasks_completions.json', 'w') as outfile:
    outfile.write(jsondata)


