import argparse
parser = argparse.ArgumentParser(description='CREATE USER for adding new user'
                                             'CREATE TASK for adding new task'
                                             'ASSIGN X Y for assigning x task to y user'
                                             'LIST USER Y for listing user y tasks'
                                             'LIST TASK X for listing users that have x task')



class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)


class Task:
    def __init__(self, name):
        self.name = name
        self.users = []

    def add_user(self, user):
        self.users.append(user)


if __name__ == '__main__':
    inp = input().split()
    tasks={}
    users={}
    while inp :
        if inp[0] == "CREATE":
            if inp[1] == "TASK":
                tasks[inp[2]] = Task(inp[2])
            elif inp[1] == "USER":
                users[inp[2]] = User(inp[2])
        elif inp[0] == "ASSIGN":
            users[inp[1]].add_task(inp[2])
            tasks[inp[2]].add_user(inp[1])
        elif inp[0] == "LIST":
            if inp[1] == "USER":
                print(users[inp[2]].tasks)
            else:
                print(tasks[inp[2]].users)
        inp = input().split()
