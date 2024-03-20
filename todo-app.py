# todo_app.py

class Todo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks

if __name__ == "__main__":
    todo = Todo()
    todo.add_task("Finish Jenkins Pipeline task")
    todo.add_task("Write Python TODO app")
    todo.add_task("Test Python TODO app")
    print("Tasks:", todo.get_tasks())

