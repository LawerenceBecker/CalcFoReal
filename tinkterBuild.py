import tkinter as tk

def buildTK(window):
    def numBut1():
        print(1)
    def numBut2():
        print(2)
    def numBut3():
        print(3)
    def numBut4():
        print(4)
    def numBut5():
        print(5)
    def numBut6():
        print(6)
    def numBut7():
        print(7)
    def numBut8():
        print(8)
    def numBut9():
        print(9)
    def numBut0():
        print(0)

    def add():
        print("add")
    def sub():
        print("sub")
    def div():
        print("div")
    def mul():
        print("mul")

    def equals():
        print("equals")

    num_butCommands = [numBut1,numBut2,numBut3,numBut4,numBut5,numBut6,numBut7,numBut8,numBut9]

    x = 1
    for i in range(3):
        for j in range(3):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i+1, column=j, padx=5, pady=5)

            button = tk.Button(master=frame, text=x, command=num_butCommands[x-1])
            x += 1
            button.pack(padx=5, pady=5)

    frame = tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame.grid(row=4, column=1, padx=5, pady=5)

    button = tk.Button(master=frame, text=0, command=numBut0)

    button.pack(padx=5, pady=5)

    frame = tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame.grid(row=1, column=3, padx=5, pady=5)

    button = tk.Button(master=frame, text="/", command=div)

    button.pack(padx=5, pady=5)

    frame = tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame.grid(row=2, column=3, padx=5, pady=5)

    button = tk.Button(master=frame, text="*", command=mul)

    button.pack(padx=5, pady=5)

    frame = tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame.grid(row=3, column=3, padx=5, pady=5)

    button = tk.Button(master=frame, text="-", command=sub)
    button.pack(padx=5, pady=5)

    frame = tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame.grid(row=4, column=3, padx=5, pady=5)

    button = tk.Button(master=frame, text="+", command=add)
    button.pack(padx=5, pady=5)

    frame = tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame.grid(row=4, column=2, padx=5, pady=5)

    button = tk.Button(master=frame, text="=", command=equals)
    button.pack(padx=5, pady=5)

    frame = tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    results = tk.Label(master=frame, text="")
    results.pack(padx=100, pady=20)