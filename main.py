import tkinter as tk
import serial
import serial.tools.list_ports


HEIGHT = 500
WIDTH = 600

def main():
    w = setup_window()
    #w.mainloop()

    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(port)

def test_function(entry):
    print("This is the entry:", entry)

def get_ports():
    return serial.tools.list_ports.comports()

def setup_window():
    # Setup window:
    root = tk.Tk()

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    background_image = tk.PhotoImage(file='landscape.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    frame = tk.Frame(root, bg='#80c1ff', bd=10)
    frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')



    lPort = tk.Label(frame, text='Port', font=30, bg='#80c1ff')
    lPort.place(relx=0.2, rely=0, anchor='n')

    # Display ports in a dropdown menu:
    ports = get_ports()
    var_ports = tk.StringVar(root)
    var_ports.set(ports[0])
    omPort = tk.OptionMenu(frame, var_ports, *ports)
    omPort.place(relx=0.5, rely=0, relheight=0.1, anchor='n')

    # Display Baudrate:
    baud_list = [110, 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 38400, 57600, 115200, 128000, 256000]
    var_baud = tk.StringVar(root)
    var_baud.set(baud_list[6])
    omBaud = tk.OptionMenu(frame, var_baud, *baud_list)
    omBaud.place(relx=0.5, rely=0.2, relheight=0.1, anchor='n')


    # Display 8N1:
    


    # Display connect button:
    bConnect = tk.Button(frame, text="Connect", font=40)
    bConnect.place(relx=0.5, rely=0.8, relheight=0.2, relwidth=0.3, anchor='n')



    root.mainloop()

    return root



if __name__ == "__main__":
    main()