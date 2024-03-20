import tkinter
from tkinter import *
root=Tk()
root.title("To-Do-List")
root.geometry( "400x650+400+100")
root.resizable(False, False)

task_list= []

def addTask(): #Function for adding the task
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert( END, task)

def deleteTask(): #Function for deleting the task
    global task_list
    task =str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("task_list.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete( ANCHOR)


def openTaskFile():#Function for open the task file

    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file=open('tasklist.txt', 'w')
        file.close()


#Designing the To Do List
#icon
Icon=PhotoImage(file="TDL Images/Icon.png") #Icon as Object Name
root.iconphoto(False,Icon)

#top bar
TopImage=PhotoImage(file="TDL Images/banner3.png")
Label(root,image=TopImage).pack()

dockImage=PhotoImage(file="TDL Images/dock.png")
Label(root,image=dockImage,bg="#000000").place(x=30,y=25)

noteImage=PhotoImage(file="TDL Images/task.png")
Label(root,image=noteImage).place(x=340,y=25)

heading=Label(root,text="ALL TASK", font="arial 20 bold", fg="BLACK", bg="#FFB30F") #FFB30F is yellow colour
heading.place(x=130, y=20)

#main
frame= Frame(root,width=400,height=40,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 14", bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="Add", font="arial 14 bold",width=8,bg="#00C957",fg="#fff", bd=0,command=addTask) #Button for adding the task
button.place(x=300,y=0)

#listbox
frame1= Frame(root,bd=3,width=700,height=280,bg="#C1C1C1")
frame1.pack(pady=(160,0))

listbox=Listbox(frame1,font=('arial', 12),width=40,height=16,bg="#98F5FF",fg="#000000",cursor="hand2",selectbackground="#007FFF")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar= Scrollbar(frame1)
scrollbar.pack(side= RIGHT ,fill= BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile() #Function call
#deletee
Delete_icon=PhotoImage(file="TDL Images/delete.png")
Button(root,image=Delete_icon, bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)
root.mainloop()