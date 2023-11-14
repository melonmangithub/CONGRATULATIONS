import tkinter as tk
import webbrowser

root = tk.Tk()
root.geometry("300x300")
root.title("CONGRATULATIONS")

n = 52
frames = [tk.PhotoImage(file = "joel-spinning.gif", format = "gif -index %i" % (i)) for i in range(n)]

def update(i):
    frame = frames[i]
    i += 1
    if (i == n): i = 0
    label.configure(image = frame)
    global time
    root.after(50, update, i)
    
def viewBlackCrimeStats():
    webbrowser.open("https://bjs.ojp.gov/content/pub/pdf/revcoa18.pdf")

tk.Label(root, text = "Congratulations, you are our lucky winner!").place(x = 10, y = 10)
label = tk.Label(root)
label.place(x = 10, y = 30, width = 280)

tk.Label(root, text = "01100001 01100111 01101111 01101110 01111001").place(x = 10, y = 190)
tk.Button(root, text = "View Black Crime Statistics", relief = tk.RIDGE, background = "gray", command = lambda: viewBlackCrimeStats()).place(x = 10, y = 265)
tk.Button(root, text = "Ok", relief = tk.RIDGE, background = "gray", command = lambda: root.destroy()).place(x = 215, y = 265, width = 75)

root.after(0, update, 0)
root.mainloop()