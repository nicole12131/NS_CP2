# NS 1st Personal Portfolio
import tkinter as tk

root = tk.Tk()
root.title("Nicole Salom - programming portfolio")
root.configure(background="white")
root.minsize(250,250)
root.maxsize(1000,1000)
root.geometry("300x300+100+100")
label = tk.Label(root, text="Programming Portfolio!", font=("Times New Roman", 14,))
label.config(fg="black", background="white")

root.count=0
def add():
    root.count += 1
    num["text"] = root.count

btn = tk.Button(root, text="ADD", command=add)
btn.pack()
num = tk.Label(root, text="0")
num.pack()
label.pack()



root.mainloop()