import tkinter


def main():
    handle_gui()


def handle_gui():
    # Setup window:
    window = tkinter.Tk()
    window.title("peterm")
    window.geometry('350x200')

    lbl = tkinter.Label(window, text="Peterm setup...")
    lbl.grid(column=0, row=0)

    def clicked():
        lbl.configure(text="Button was clicked !!")

    btn = tkinter.Button(window, text="Click Me", command=clicked)

    btn.grid(column=1, row=0)

    lbl2 = tkinter.Label(text="Second row param")

    lbl2.grid(column=1, row=1)


    window.mainloop()





if __name__ == "__main__":
    main()