import tkinter as tk
from oop import oop
import os

def addValues(event):

    selected_index = listbox.curselection()[0]
    selected_value = listbox.get(selected_index)

    additional_listbox.delete(0, 'end')
    additional_values = inf.checkDir(selected_value, main=True)
    
    entry.delete(0, 'end')
    entry.insert(0, selected_value + ' / ')

    inf.resetDir()
    inf.changeDir(dirName=selected_value)

    for value in additional_values:
        additional_listbox.insert('end', value)
        if os.path.isdir(value):
            additional_listbox.bind(f"<ButtonRelease-1>", underValues)
        else: 
            additional_listbox.bind(f"<ButtonRelease-1>", openFile)


def underValues(event):

    selected_index = additional_listbox.curselection()[0]
    selected_value = additional_listbox.get(selected_index)

    additional_listbox.delete(0, 'end')
    additional_values = inf.checkDir(selected_value)

    entry.insert('end', selected_value + ' / ')

    inf.changeDir(dirName=selected_value)
    print(os.getcwd())

    for value in additional_values:
        additional_listbox.insert('end', value)

        if os.path.isdir(value):
            additional_listbox.bind(f"<ButtonRelease-1>", underValues)
        else: 
            additional_listbox.bind(f"<ButtonRelease-1>", openFile)

def openFile(event):
    selected_index = additional_listbox.curselection()[0]
    selected_value = additional_listbox.get(selected_index)
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
        print(f"{selected_index}\n{valuesInd[i][1]}\n{valuesInd[i][2]}\nsize:{len(valuesInd)}")
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
        if os.path.isdir(value):
            additional_listbox.bind(f"<ButtonRelease-1>", underValues)
        else: 
            additional_listbox.bind(f"<ButtonRelease-1>", openFile)

inf = oop()

root = tk.Tk()

#Название сверху окна
root.title("SearchApp")

#Размер окна по умолчанию
root.geometry('1000x700')

#Левая часть окна
listbox = tk.Listbox(root, font=30, width=50)
listbox.grid(column=0, row=1, ipadx=10, ipady=10)

values = inf.checkDir()

for value in values:
    listbox.insert(tk.END, value)
    listbox.bind(f"<ButtonRelease-1>", addValues)

additional_listbox = tk.Listbox(root, font=30, width=50)
additional_listbox.grid(column=1, row=1, columnspan=1, ipadx=10, ipady=10)

entry = tk.Entry(root, width=100, font=30)
entry.grid(column=0, columnspan=2, row=0, ipadx=10, ipady=10)
entry.insert(0, "")
entry.bind("<ButtonRelease-1>", on_click)



#Бесконечный цикл работы
root.mainloop()




