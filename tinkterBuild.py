import tkinter as tk

value = 0
method = ""
on = True
def buildTK(window):
    
    ### Off On button
    def OnOff():
        global on
        if on:
            on = False
            results.config(bg = "black")
            for b in all_but:
                b["state"] = "disable"
        else:
            on = True
            results.config(bg = "#F0EDE2")
            for b in all_but:
                b["state"] = "normal"

    ### All num Buttons
    def numBut1():
        if method == "equals":
            results["text"] = "1"
        else:
            results["text"] += "1"
    def numBut2():
        if method == "equals":
            results["text"] = "2"
        else:
            results["text"] += "2"
    def numBut3():
        if method == "equals":
            results["text"] = "3"
        else:
            results["text"] += "3"
    def numBut4():
        if method == "equals":
            results["text"] = "4"
        else:
            results["text"] += "4"
    def numBut5():
        if method == "equals":
            results["text"] = "5"
        else:
            results["text"] += "5"
    def numBut6():
        if method == "equals":
            results["text"] = "6"
        else:
            results["text"] += "6"
    def numBut7():
        if method == "equals":
            results["text"] = "7"
        else:
            results["text"] += "7"
    def numBut8():
        if method == "equals":
            results["text"] = "8"
        else:
            results["text"] += "8"
    def numBut9():
        if method == "equals":
            results["text"] = "9"
        else:
            results["text"] += "9"
    def numBut0():
        if method == "equals":
            results["text"] = "0"
        else:
            results["text"] += "0"

    ### All math funcs Buttons
    def add():
        global value
        global method
        method = "add"
        value = float(results["text"])
        results["text"] = ""
    def sub():
        global value
        global method
        method = "sub"
        value = float(results["text"])
        results["text"] = ""
    def div():
        global value
        global method
        method = "div"
        value = float(results["text"])
        results["text"] = ""
    def mul():
        global value
        global method
        method = "mul"
        value = float(results["text"])
        results["text"] = ""
    def dec():
        if method == "equals":
            results["text"] = "."
        else:
            results["text"] += "."

    ### Equal Button
    def equals():
        global value
        global method
        if method == "add":
            res = value + float(results["text"])
        elif method == "sub":
            res = value - float(results["text"])
        elif method == "div":
            res = value / float(results["text"])
        elif method == "mul":
            res = value * float(results["text"])
        method = "equals"
        results["text"] = str(res)
        value = 0

    ### Clear button
    def clear():
        global value
        global method
        value = 0
        method = ""
        results["text"] = ""

    ### Make all buttons
    num_butCommands = [numBut1,numBut2,numBut3,numBut4,numBut5,numBut6,numBut7,numBut8,numBut9, numBut0, div, mul, sub, add , dec, equals]
    
    all_but = []

    botFrame = tk.Frame(master=window)

    rowNum = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 2, 2, 3, 3, 4, 4]
    colNum = [0, 1, 2, 0, 1, 2, 0, 1, 2, 1, 3, 4, 4, 3, 4, 3]
    textNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '/', "*", "-", "+", ".", "="]
    x = 0
    for bC in num_butCommands:
        frame = tk.Frame(
            master=botFrame,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=rowNum[x], column=colNum[x], padx=5, pady=5)

        button = tk.Button(master=frame, text=textNum[x], command=bC)
        all_but.append(button)
        x += 1
        button.pack(padx=5, pady=5)

    ### Clear Buttons
    frame = tk.Frame(
        master=botFrame,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame.grid(row=1, column=3, columnspan=2, padx=5, pady=5)

    button = tk.Button(master=frame, text="C", command=clear)

    button.pack(padx=30, pady=5)

    ### On Off Button
    frame = tk.Frame(
        master=botFrame,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame.grid(row=4, column=0, padx=5, pady=5)

    button = tk.Button(master=frame, text="O/F", command=OnOff)
    button.pack(padx=5, pady=5)

    ### Make Result Label
    topFrame = tk.Frame(master=window)

    rFrame = tk.Frame(
        master=topFrame,
        relief=tk.RAISED,
        borderwidth=1
    )
    rFrame.grid(row=0, column=0, columnspan=4)

    results = tk.Label(master=rFrame, text="", width=25, height=4, bg="#F0EDE2")
    results.pack()

    topFrame.grid(row=0)
    botFrame.grid(row=1)