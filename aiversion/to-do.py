import json

try:
    f = open("tasks.json", "r")
    tasks = json.load(f)
    f.close()
except:
    tasks = []

while True:
    print("\n1. Add  2. View  3. Delete  4. Exit")
    choice = input("Choice: ")
    
    if choice == "1":
        task = input("Task: ")
        tasks = tasks + [task]
        f = open("tasks.json", "w")
        json.dump(tasks, f)
        f.close()
        print("Added!")
    elif choice == "2":
        if len(tasks) > 0:
            for i in range(len(tasks)):
                print(str(i+1) + ". " + tasks[i])
        else:
            print("No tasks")
    elif choice == "3":
        for i in range(len(tasks)):
            print(str(i+1) + ". " + tasks[i])
        try:
            num = int(input("Delete number: "))
            tasks = tasks[:num-1] + tasks[num:]
            f = open("tasks.json", "w")
            json.dump(tasks, f)
            f.close()
            print("Deleted!")
        except:
            print("Invalid!")
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
