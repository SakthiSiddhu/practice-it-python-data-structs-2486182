
from collections import deque
task_list = deque(maxlen=5)
class Task(object):
    def __init__(self,desc,priority=False):
        self.desc=desc
        self.priority=priority
    

    def add_task(self):
        if self.priority:
            task_list.appendleft(self)
        else:
            task_list.append(self)
    


    def __str__(self):
        return "Task desc - {0} : Task Priority - {1}".format(self.desc,self.priority)
def main():
    #add code here
    t1 = Task('Buy things',True)
    t2= Task('go out')
    t3= Task('write',True)
    t1.add_task()
    t2.add_task()
    t3.add_task()

    for task in task_list:
        print(task)
    return

if __name__ == "__main__":
    main()