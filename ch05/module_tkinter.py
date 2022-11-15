"""
import tkinter as tk    #tkinter를 tk라 할거다

s = "Hello world! \n I am suk."

root = tk.Tk()
t = tk.Text(root, height=10, width=30)
t.insert(tk.END, s) #s 내용을 삽입
t.pack()
tk.mainloop()
"""
#################################################
# 2021년 3월 달력을 표시하는 창을 띄워라

import tkinter as tk
import calendar

cal = calendar.TextCalendar()
view = cal.formatmonth(2021, 3)

root = tk.Tk()
t = tk.Text (root, height=10, width=30)
t.insert(tk.END, view)
t.pack()
tk.mainloop()

