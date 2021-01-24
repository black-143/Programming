#!/usr/bin/env python3

from datetime import datetime

import sys

todoFile, doneFile = open("todo.txt", "a"), open("done.txt", "a")

def main_menu():
	"""
	    This function prints the menu of the todo list.
	"""
	print(
"""
Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics""")


def add():
	"""
        This function adds the task into the file todo.txt
    """
	try:
	    task = sys.argv[2]
	    file = open("todo.txt", "a")
	    file.write(task + "\n")
	    print('Added todo: "{}"'.format(task))
	except IndexError:
	    print("Error: Missing todo string. Nothing added!")


def getTasks():
	"""
        This function reads the file from todo.txt and prints it
        onto the screen
    """
	tasks = open("todo.txt").readlines()
	if len(tasks):
	    for num in range(len(tasks) - 1, -1, -1):
	        print("[%d] %s" % (num + 1, tasks[num]), end="")
	else:
	    print("There are no pending todos!")


def markOff(isdelete = 0):
	"""
        This function stikes off the task which is done and deletes it from todo.txt
        and adds it to done.txt.

        :param isdelete: to act differently when del command is run at command line.
        :type isdelete: int
        :default value: 0
    """
	try:
	    taskId = sys.argv[2]
	    tasks = open("todo.txt").readlines()
	    file = open("todo.txt", "w")
	    doneTasks = open("done.txt", "a")
	    flag = True
	    for task in range(len(tasks)):
	        if task + 1 == int(taskId):
	        	flag = False
	        	if isdelete == 1:
	        		continue
	        	elif isdelete == 0:
	        		data = "x {} {}".format(datetime.today().strftime("%d/%m/%Y"), tasks[task])
	        		doneTasks.write(data)
	        else:
	        	file.write(tasks[task])

	    if not isdelete:
	    	if flag:print("Error: todo #%s does not exist." % (taskId))
	    	else:print("Marked todo #%s as done." % (taskId))
	    
	    if isdelete:
	    	if flag:print("Error: todo #%s does not exist. Nothing deleted." %(taskId))
	    	else:print("Deleted todo #%s" % (taskId))

	except IndexError:
		if isdelete:print("Error: Missing NUMBER for deleting todo.")
		else:print("Error: Missing NUMBER for marking todo as done.")


def deleteTask():
	"""
        This function need is similar to markOff function so calls it by
        passing isdelete = 1 as argument.
    """
	markOff(isdelete = 1)        


def getReport():
	"""
        This function prints the pending and done tasks
    """
	pending = len(open("todo.txt").readlines())
	done = len(open("done.txt").readlines())
	print(
	    "{} Pending : {} Completed : {}"
	    .format(datetime.today().strftime("%Y-%m-%d"),
	            pending,
	            done
	            ))


def main():
	"""
        This function calls the other functions based on command issued.
    """
	n = len(sys.argv)
	if n == 1:
	    main_menu()
	elif n > 3:
	    print("Invalid number of args")
	else:
	    features = {
	        "add": add,
	        "help": main_menu,
	        "ls": getTasks,
	        "done": markOff,
	        "report": getReport,
	        "del": deleteTask}
	    choosedFeature = features.get(sys.argv[1],"Invalid Argument")
	    if choosedFeature == "Invalid Argument":
	    	print(choosedFeature)
	    else:
	    	choosedFeature()


if __name__ == "__main__":
    main()
