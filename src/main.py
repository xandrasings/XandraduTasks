from service import todoist_service, habitify_service

habit_task_completions = todoist_service.get_habit_task_completions()
habit_behavior = habitify_service.generate_habit_behavior(habit_task_completions)
habitify_service.update_habitify(habit_behavior)

