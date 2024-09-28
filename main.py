import tkinter as tk
import random

root = tk.Tk()
root.geometry('600x500')
frame = tk.Frame(root)
frame.pack()


#LEFT SIDE

leftFrame = tk.Frame(master=root, width=(600*0.4), bg="red")
leftFrame.pack(fill=tk.Y, side=tk.LEFT)
leftFrame.pack_propagate(False)

recordBtn = tk.Button(leftFrame, text="Record", height=1,bg="blue")
recordBtn.pack(fill=tk.X, side=tk.BOTTOM)

stopStartBtn = tk.Button(leftFrame, text="Stop/Start", height=1,bg="blue")
stopStartBtn.pack(fill=tk.X, side=tk.BOTTOM)

#RIGHT SIDE

rightFrame = tk.Frame(master=root, width=(600*0.6), bg="yellow")
rightFrame.pack(fill=tk.Y, side=tk.RIGHT)
rightFrame.grid_propagate(False)
rightFrame.rowconfigure(0, minsize=50)

frame3 = tk.Frame(master=rightFrame, width=600, height = 50, bg="green")
frame3.grid(row=0, column=0, rowspan=1)

frame3 = tk.Frame(master=rightFrame, width=600, height=50, bg="purple")
frame3.grid(row=1, column=0, rowspan=1)

frame3 = tk.Frame(master=rightFrame, width=600, height=400, bg="teal")
frame3.grid(row=2, column=0, rowspan=1)
frame3.pack_propagate(False)

timeline_xthing2 = int(600*0.6*0.1)
timeline_xthing = timeline_xthing2/2

timeline = tk.Listbox(master=frame3, width=int(timeline_xthing2), height=22, bg="pink")
timeline.place(x=timeline_xthing, y=0)
timeline.pack_propagate(False)
#(timeline_xthing/2)

timelineScrollbar = tk.Scrollbar(timeline, orient="vertical", command=timeline.yview)
timelineScrollbar.pack(side=tk.RIGHT, fill=tk.Y)
timeline.configure(yscrollcommand=timelineScrollbar.set)

# skibidi
agc = ['intro', 'jennifer\'s body', 'hardcore', 'pouring out the syrup', 'singapore', 'it\'s over', 'smthn talkin', 'like this', 'paranoid', 'interlude', 'fyt', 'so dark', 'ken carson', 'outro'] * 3

for i in range(len(agc)):
    timeline.insert(i, agc[i])


root.mainloop()