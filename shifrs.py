from tkinter import *


def goDecode():
    if rBtn.get() == 0 or rBtn.get() == 1:
        goCode()
    else:
        tOutput.delete(1.0, END)
        tIn = tInput.get(1.0, END)
        tIn = tIn[0:len(tIn) - 1]
        tOut = ""
        if rBtn.get() == 2:
            for i in range(len(tIn)):
                tOut += chr(ord(tIn[i]) - 1)
        elif rBtn.get() == 3:
            p = 0
            for i in range(len(tIn)):
                tOut += chr(ord(tIn[i]) - p)
                p = (p + 1) % 33
        tOutput.insert(1.0, tOut)


def goCode():
    tOutput.delete(1.0, END)
    tIn = tInput.get(1.0, END)
    # Убираем перенос строки
    tIn = tIn[0:len(tIn) - 1]
    tOut = ""
    if rBtn.get() == 0:
        for i in range(len(tIn) - 1, -1, -1):
            tOut += tIn[i]
    elif rBtn.get() == 1:
        for i in range(0, len(tIn) - 1, 2):
            tOut += tIn[i + 1] + tIn[i]
    elif rBtn.get() == 2:
        for i in range(len(tIn)):
            tOut += chr(ord(tIn[i]) + 1)
    elif rBtn.get() == 3:
        p = 0
        for i in range(len(tIn)):
            tOut += chr(ord(tIn[i]) + p)
            p = (p + 1) % 33
    tOutput.insert(1.0, tOut)


def clearText():
    tInput.delete(1.0, END)
    tOutput.delete(1.0, END)


def resToDef():
    tInput.delete(1.0, END)
    txt = tOutput.get(1.0, END)
    txt = txt[0:len(txt) - 1]
    tInput.insert(1.0, txt)


def pasteFromClipboard():
    try:
        tInput.insert(END, root.clipboard_get())
    except:
        tInput.insert(END, "\nОшибка: Буфер пуст")


def copyToClipboard():
    root.clipboard_clear()
    root.clipboard_append(tOutput.get(1.0, END))


def setMenuPos(event):
    menuInput.post(event.x_root, event.y_root)


# Инициализация окна
root = Tk()
root.resizable(False, False)
root.title("Шифровщик")

# Настройка геометрии окна
WIDTH = 800
HEIGHT = 320

SCR_WIDTH = root.winfo_screenwidth()  # Ширина экрана в пикселях
SCR_HEIGHT = root.winfo_screenheight()

POS_X = SCR_WIDTH // 2 - WIDTH // 2  # Координата по X
POS_Y = SCR_HEIGHT // 2 - HEIGHT // 2  # Координата по Y

root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
# Текстовые метки
textInput = Label(text="Введите исходный текст:")
textInput.place(x=2, y=1)
textOutput = Label(text="Результат:")
textOutput.place(x=2, y=157)

# Текстовые поля
tInput = Text(width=70, height=8, wrap=WORD)
tInput.place(x=5, y=20)
tInput.insert(1.0, """Экземпляры Checkbutton также могут быть визуально оформлены в группу, но каждый флажок 
независимы от остальных. Каэждый может быть в состоянии 'устновлен' или 'снят', независимо от состояний других 
флажков. Другими словами, в группе Checkbutton можно сделать множественный выбор, в группе Radiobutton - нет""")

scrollInput = Scrollbar(command=tInput.yview, width=20)
scrollInput.place(x=570, y=20, height=132)
tInput["yscrollcommand"] = scrollInput.set

tOutput = Text(width=70, height=8, wrap=WORD)
tOutput.place(x=5, y=180)

scrollOutput = Scrollbar(command=tOutput.yview, width=20)
scrollOutput.place(x=570, y=180, height=123)
tOutput["yscrollcommand"] = scrollOutput.set

# Меню на правую кнопку
menuInput = Menu(tearoff=False)
menuInput.add_command(label="Копировать результат", command=copyToClipboard)
menuInput.add_command(label="Вставить в исходный текст", command=pasteFromClipboard)
menuInput.add_command(label="Результат -> Исходный", command=resToDef)
menuInput.add_command(label="Очистить текст", command=clearText)
tInput.bind("<Button-3>", setMenuPos)

btnCode = Button(text="Шифровать", width=25, command=goCode)
btnCode.place(x=600, y=20)

btnDecode = Button(text="Дешифровать", width=25, command=goDecode)
btnDecode.place(x=600, y=50)

# Радиокнопки
textAlgo = Label(text="Алгоритм:")
textAlgo.place(x=600, y=100)
rBtn = IntVar()
rBtn.set(0)
algo01 = Radiobutton(text="Инвертировать", variable=rBtn, value=0)
algo02 = Radiobutton(text="Замена с соседней", variable=rBtn, value=1)
algo03 = Radiobutton(text="+1", variable=rBtn, value=2)
algo04 = Radiobutton(text="+позиция (до 33)", variable=rBtn, value=3)
algo01.place(x=600, y=120)
algo02.place(x=600, y=140)
algo03.place(x=600, y=160)
algo04.place(x=600, y=180)

root.mainloop()
