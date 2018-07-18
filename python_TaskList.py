import os
os.system("clear")

import datetime
now = datetime.datetime.now()

greeting = ("Congratulations! You're running PJ's Task List program. \n")

name = input("What is your filename? ").lower()

my_file = open(name+"userList.txt","a+")

my_file.write(str(now))


text = open(name+"userList.txt", "r").read()



print("Hello, this was your last session: \n" + text)

class User():
    def __init__(self, tasks=[]):
        self.userTasks = tasks


def main():
    profile = User()
    print (greeting)
    profile.userTasks.append(input("\nEnter a Task: "))

    while True:
        modifyList = input("\nWould you like to 'add' a task, 'remove' a task, 'check' your current list, or 'quit' the program and save?: ").lower()
        if modifyList!="remove" and modifyList!="add" and modifyList!="quit" and modifyList!="check":
            print("Please input either 'add', 'remove', 'check', or 'quit'")
            continue
        elif modifyList == "add":
            profile.userTasks.append(input("\n Input a new task: "))
            continue
        elif modifyList == "remove":
            profile.userTasks.pop(int(input("\nWhich task do you want to remove: ")))
            continue
        elif modifyList == "check":
            for pretty in profile.userTasks:
                print(text)
                print("\n" + pretty)
            continue
        elif modifyList == "quit":
            end=(input("\nThanks for running my program! Please sign your name to end: "))
            break
        else:
            print("an unexpected error occurred")
            break
    print("\nUser name is: " + end + "\n")
    print("Your finished createing this list is: ", profile.userTasks)
    my_file.write("\nUser name is: " + end + "\n")
    for info in profile.userTasks:
        my_file.write(info + "\n")
    my_file.write("The date is: " + "\n" + "_______________________" + "\n")


if __name__ == '__main__':
    main()