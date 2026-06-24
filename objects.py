class Task:


    def __init__(self, task, priority = 3, category = 'None', status = False, false_id=0):
        self.id = false_id
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

    def to_dict(self):
        task_json = {
            'id': self.id,
            'name': self.task,
            'category': self.category,
            'priority': self.priority,
            'status': self.status
        }
        return task_json