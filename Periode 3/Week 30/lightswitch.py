import tkinter as tk
window = tk.Tk()
light_on=False
def switchLight():
    global light_on
    if light_on:
        button.config(text='Switch light on')
        window.config(bg='black')
        light_on=False
        print('Light is off')
    else:
        button.config(text='Switch light off')
        window.config(bg='yellow')
        light_on=True
        print('Light is on')
button = tk.Button(text='Switch light on', bg="white", fg="black",command=switchLight)
button.pack(pady = 20, padx = 20)

window.mainloop()