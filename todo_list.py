# User Interface (UI):
# Display a welcoming message and a menu with the following options:


# To-Do List Features:
# Implement the following features for the To-Do List:
# Adding a task with a title (by default “Incomplete”).
# Viewing the list of tasks with their titles and statuses (e.g., "Incomplete" or "Complete").
# Marking a task as complete.
# Deleting a task.
# Quitting the application.
print("WELCOME TO THE TO-DO LIST APPLICATION!")
print()
def displayMenu():
    while True:
        try:
            userChoice = input(""" 
            ***TASKS MUST BE COMPLETED IN ORDER***
            1. Add a task
            2. View tasks
            3. Mark a task as complete
            4. Delete a task
            5. Quit\n""")
            userChoice = int(userChoice)
        except ValueError:
            print("ERROR: Please enter number listed in menu!")
        
        if userChoice == 1:
            def addTask():
                title = []
                statusI = " - Incomplete"
                # statusC = " Complete" 
                counter = 1  
                anotherItem = 'Y'
                userExit = False
                while anotherItem.upper() == 'Y' or userExit:
                    longerItem = 'Y'
                    while True:
                        try:
                            itemToAdd = input("Enter item: ") 
                            if itemToAdd == "":
                                raise Exception("ERROR: At least 1 task must be added to list!")  
                            if len(itemToAdd) <= 2:
                                print("ERROR: Task must be 3 characters or longer!") 
                                reEnter = input("Re-enter item or exit (Y or N): ") 
                                if reEnter.upper() == "N":
                                    userExit = True
                                    break
                                continue
                            break  
                        except Exception as e:
                            print(e)   
                    if userExit == True:
                        break
                    if len(itemToAdd) > 2:
                        itemToAdd = itemToAdd.capitalize()
                        itemToAdd
                        title.append(f"Task {counter}:" + " " + itemToAdd + statusI)
                        counter = counter + 1
                        anotherItem = input("Add another item (Y or N): ")
                        
                return "\n".join(map(str, title))
            listOfTasks = addTask()
        elif userChoice == 2 and not listOfTasks == "":
            def viewTasks():
                print()
                print("*****UPDATED TO-DO LIST*****\n")
                print(listOfTasks)
    
            if not listOfTasks == "":
                viewTasks()
                print()
        elif userChoice == 3 and not listOfTasks == "":
            def updateTask(listOfTasks):
                updateAnother = 'T'
                viewTasks()
                listOfTasks = listOfTasks.split('\n')
                
                while updateAnother == 'T':
                    while True: 
                        taskNum = input("Enter number of task to update or E for exit: ")
                        if taskNum == 'E':
                            return "\n".join(map(str, listOfTasks))
                        checkForNum = any(taskNum in string for string in listOfTasks)
                        checkForInc = any("Incomplete" in string for string in listOfTasks)
                        if not checkForNum:
                            print('ERROR: Task does not exist!')
                            continue
                        if checkForNum and checkForInc:
                            listOfTasks = [string.replace("Incomplete", "Complete") if taskNum in string else string for string in listOfTasks]
                        stringNum = len([string for string in listOfTasks if isinstance(string,str)])
                        print(f"Task {int(taskNum)} Updated!")
                        allComplete = all("Complete" in string for string in listOfTasks)
                        if allComplete:
                            break
                        if not stringNum == 1:
                            updateAnother = input("Would you like to update another task? T or F: ")
                            if updateAnother == 'T':
                                continue
                            if updateAnother.upper() == 'F':
                                break 
                        if updateAnother.upper() == 'T' and stringNum == 1:
                            if checkForNum and not checkForInc:
                                print("ERROR: Task already complete!")
                        break
                    break         
                print()
                print("*****UPDATED TO-DO LIST*****")
                print()
                return "\n".join(map(str, listOfTasks))
            updateTask = updateTask(listOfTasks)
            print(updateTask)
        elif userChoice == 4 and not updateTask == "":  
            def deleteTask(updateTask):
                print(updateTask)
                deleteTask = updateTask.split('\n')
                deleteAnother ='T'
                    
                while deleteAnother:    
                    taskNum = input("Enter number of task to delete: ")
                    checkForNum = any(taskNum in string for string in deleteTask)
                    deleteTask = [string for string in deleteTask if not taskNum in string]
                    deleteTask = [f"Task {i + 1}: " + string.split(":", 1)[1] for i , string in enumerate(deleteTask)]
                    deleteAnother = input("Would you like to delete another? T or F: ")

                    while not deleteAnother.upper() == 'T' and not deleteAnother.upper() == 'F':
                        deleteAnother = input("ERROR: 'Enter 'T' or 'F' to delete another task:  ")
                    if deleteAnother.upper() == 'F':
                        break
                    if deleteTask == []:
                        print("There are no tasks to complete!")
                        break
                    else:
                        continue
                print()
                print("*****UPDATED TO-DO LIST*****")
                print()
                return "\n".join(map(str, deleteTask))        
            print(deleteTask(updateTask))
        elif userChoice == 5:
            print("Application terminated! ")
            break
displayMenu()

