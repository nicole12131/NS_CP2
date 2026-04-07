import tkinter as tk
count = 0

root = tk.Tk()

root.title("Testing")
root.configure(background="orange")
root.minsize(250,250)
root.maxsize(1000,1000)
root.geometry("300x300+100+100")
label = tk.Label(root, text="This is currently working!", font=("Times New Roman", 14, "bold"))
label.config(fg="blue", background="orange")
# stuff about botton
root.count=0
def add():
    root.count += 1
    num["text"] = root.count

btn = tk.Button(root, text="ADD", command=add)
btn.pack()
num = tk.Label(root, text="0")
num.pack()
label.pack()


label.pack()
#image = tk.PhotoImage(file="notes/twice.jpeg")
#tk.Label(root, image=image).pack()

root.mainloop()