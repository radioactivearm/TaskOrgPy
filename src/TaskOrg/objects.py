class Task:
    def __init__(self, task, priority = 3, status = False):
        self.task = task
        self.priority = priority
        self.status = status

    def print(self):
        check = " "
        if self.status:
            check = "x"
        print(f"{self.task} [{check}]")

    def set_priority(self, new_priority):
        self.priority = new_priority