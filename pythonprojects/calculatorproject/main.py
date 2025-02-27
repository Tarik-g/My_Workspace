import tkinter as tk

def add():
    pass

def subtract():
    pass

def divide():
    pass

def multiply():
    pass

#erstelle Window
window = tk.Tk()

window.geometry("500x650")
window.title("Calculator")

button_frame = tk.Frame(window)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)
button_frame.columnconfigure(3, weight=1)
button_frame.pack(fill="x")



add_button = tk.Button(button_frame, text="+")
add_button.grid(row=0,column=0, sticky=tk.W+tk.E)

subtract_button = tk.Button(button_frame, text="-")
subtract_button.grid(row=0,column=1, sticky=tk.W+tk.E)

multiply_button = tk.Button(button_frame, text="*")
multiply_button.grid(row=0,column=0, sticky=tk.W+tk.E)

divide_button = tk.Button(button_frame, text="/")
divide_button.grid(row=0,column=1, sticky=tk.W+tk.E)

add_button = tk.Button(button_frame, text="+")
add_button.grid(row=0,column=0, sticky=tk.W+tk.E)

subtract_button = tk.Button(button_frame, text="-")
subtract_button.grid(row=0,column=1, sticky=tk.W+tk.E)

add_button = tk.Button(button_frame, text="+")
add_button.grid(row=0,column=0, sticky=tk.W+tk.E)

subtract_button = tk.Button(button_frame, text="-")
subtract_button.grid(row=0,column=1, sticky=tk.W+tk.E)

add_button = tk.Button(button_frame, text="+")
add_button.grid(row=0,column=0, sticky=tk.W+tk.E)

subtract_button = tk.Button(button_frame, text="-")
subtract_button.grid(row=0,column=1, sticky=tk.W+tk.E)

add_button = tk.Button(button_frame, text="+")
add_button.grid(row=0,column=0, sticky=tk.W+tk.E)

subtract_button = tk.Button(button_frame, text="-")
subtract_button.grid(row=0,column=1, sticky=tk.W+tk.E)

if __name__ == '__main__':
    window.mainloop()


#solange Prgroamm läuft:
#anzeigen was eingegeben wurde
# osbald = gedrückt Ergebnis anzeigen
for input in inputs:
    pass

# numbers 0 to 9

# löschen alles

# calculate