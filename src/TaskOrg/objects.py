class Task:
    def __init__(self, task, category = 'None', priority = 3, status = False):
        self.task = task
        self.category = category
        self.priority = priority
        self.status = status

    def print(self):
        check = " "
        if self.status:
            check = "x"
        print(f"{self.task} [{check}]")

    def set_priority(self, new_priority):
        self.priority = new_priority

    def complete(self):
        self.status = True

    def to_json(self):
        task_json = {
            'name': self.task,
            'category': self.category,
            'priority': self.priority,
            'status': self.status
        }
        return task_json