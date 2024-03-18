import tkinter as tk
from tkinter import Canvas
from tkinter import PhotoImage
from tkinter import filedialog as fld
from oop import oop
import os
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from tkinter import ttk


def addValues(event):

    selected_index = listbox.curselection()[0]
    selected_value = listbox.get(selected_index)
    
    inf.resetDir()

    if os.path.isdir(selected_value):
        additional_listbox.delete(0, 'end')
        additional_values = inf.checkDir(selected_value, main=True)
        
        entry.delete(0, 'end')
        entry.insert(0, selected_value + ' / ')

        inf.changeDir(dirName=selected_value)

        for value in additional_values:
            additional_listbox.insert('end', value)
            additional_listbox.bind(f"<ButtonRelease-1>", openFileOrDir)
    else:
        inf.openFile(selected_value)

def openFileOrDir(event):
    selected_index = additional_listbox.curselection()[0]
    selected_value = additional_listbox.get(selected_index)

    if os.path.isdir(selected_value):
        additional_listbox.delete(0, 'end')
        additional_values = inf.checkDir(selected_value)

        entry.insert('end', selected_value + ' / ')

        inf.changeDir(dirName=selected_value)
        #print(os.getcwd())

        for value in additional_values:
            additional_listbox.insert('end', value)
            additional_listbox.bind(f"<ButtonRelease-1>", openFileOrDir)
    else:
        inf.openFile(selected_value)

def on_click(event):
    valuesInd = []
    value = entry.get()
    j = 0
    for i in range(len(value)):
        if value[i] == '/':
            valuesInd.append([value[j:i], j, i])
            j = i + 1
    values = value.split(' / ')
    selected_index = entry.index('insert')
    selected_value = ""
    for i in range(len(valuesInd)):
        valuesInd[i][0] = valuesInd[i][0].replace(" ", "")
        #print(f"{selected_index}\n{valuesInd[i][1]}\n{valuesInd[i][2]}\nsize:{len(valuesInd)}")
        if selected_index in range(valuesInd[i][1], valuesInd[i][2]):
            selected_value = valuesInd[i][0]
    vals = values[:values.index(selected_value)+1]
    str1 = ''
    str2 = ''
    for i in range(len(vals)):
        str1+= vals[i] + "\\"
    for i in range(len(vals)):
        if i == len(vals)-1:
            str2+= vals[i]
        else:
            str2+= vals[i] + " / "
    entry.delete(0 , 'end')
    entry.insert(0, str2 + " / ")
    inf.resetDir()
    inf.changeDir(dirName=str1)
    additional_listbox.delete(0, 'end')
    additional_values = inf.checkDir()

    for value in additional_values:
        additional_listbox.insert('end', value)
        additional_listbox.bind(f"<ButtonRelease-1>", openFileOrDir)

def rightClickMenu(event):
    global extra_menu
    extra_menu = tk.Menu(root, tearoff=0)
    extra_menu.add_command(label="Создать директорию", command=rightClick)
    extra_menu.add_command(label="Создать файл", command=rightClick)
    extra_menu.add_command(label="Добавить файл", command=lambda:RCM_addFile())
    extra_menu.add_command(label="Открыть", command=lambda:RCM_open())
    extra_menu.add_command(label="Копировать", command=rightClick)
    extra_menu.add_command(label="Вставить", command=rightClick)
    extra_menu.add_command(label="Удалить", command=lambda:RCM_delete())
    extra_menu.post(event.x_root, event.y_root)

def rightClick():
    showinfo(title="Информация", message="Находится в разработке")
    extra_menu.unpost()

def RCM_open():
    fl = fld.askopenfilename(initialdir=inf.currentDir, title=openTitle)
    if fl:
        os.system(f"start {fl}")
    extra_menu.unpost()

def RCM_addFile():
    fl = fld.askopenfilename(title=openTitle)
    os.system(f"copy {fl} {inf.currentDir}")
    extra_menu.unpost()

def RCM_delete():
    fl = fld.askopenfilename(title=openTitle)
    if os.path.isdir(fl):
        os.system(f"rm {fl}")
    else:
        os.system(f"del {fl}")
    extra_menu.unpost()

def createAll():
    os.system("mkdir C:\\SearchApp")
    os.system("mkdir C:\\SearchApp\\Взводы")
    os.system("mkdir C:\\SearchApp\\Взводы\\СЗ-1523")
    os.system("mkdir C:\\SearchApp\\Взводы\\СЗ-1123")
    os.system("mkdir C:\\SearchApp\\Взводы\\СЗ-3024")

    os.system("mkdir C:\\SearchApp\\Презентации")

    os.system("mkdir C:\\SearchApp\\Документы")

    os.system("mkdir C:\\SearchApp\\Фотографии")

createAll()

openTitle = "Выбор файла"

inf = oop()

root = tk.Tk()

#Название сверху окна
root.title("SearchApp")

#Размер окна по умолчанию
root.geometry('1000x700')

#Левая часть окна
listbox = tk.Listbox(root, font="Times 17", width=43, height=20, activestyle=tk.NONE, selectmode="SINGLE")

values = inf.checkDir()

for value in values:
    listbox.insert(tk.END, value)
    listbox.bind(f"<ButtonRelease-1>", addValues)  

listbox.bind(f"<Button-3>", rightClickMenu)

additional_listbox = tk.Listbox(root, font="Times 17", width=40, height=20, activestyle=tk.NONE, selectmode="SINGLE")
scrollbar = ttk.Scrollbar(orient="vertical",command=additional_listbox.yview)
additional_listbox["yscrollcommand"]=scrollbar.set

additional_listbox.bind(f"<Button-3>", rightClickMenu)



entry = tk.Entry(root, width=87, font="Times 17")
entry.insert(0, "")
entry.bind("<ButtonRelease-1>", on_click)


###
#image = Image.open("C:\\Users\\12345\\Desktop\\temchik\\images\\bg.jpg")
#bg = ImageTk.PhotoImage(image)
#canvas1 = Canvas(root, width = 1000, height = 700) 
#canvas1.pack(fill = "both", expand = True) 
#canvas1.create_image( 0, 0, image = bg, anchor = "nw") 
###



entry.grid(column=0, columnspan=2, row=0, ipady=10, ipadx=20)
listbox.grid(column=0, row=1, ipadx=10)
additional_listbox.grid(column=1, row=1, ipadx=10)
scrollbar.grid(column=2, row=1)


#Бесконечный цикл работы
root.mainloop()




