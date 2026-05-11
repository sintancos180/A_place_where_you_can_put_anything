import tkinter as tk
from tkinter import messagebox
import random
cheers = ["오늘 하루도 고생 많았어",
          "성적은 숫자에 불과해. 너의 가치는 그보다 훨씬 커.",
          "잠시 쉬어도 좋아. 내일의 너는 오늘보다 더 멋질거야.",
          "포기하지 않고 다시 시작하는 그 마음이 바로 역전의 기회야.",
          "오늘은 푹 쉬고, 내일 조금 더 가벼운 마음으로 시작해보자."]
def show_message():
    message = random.choice(cheers)
    messagebox.showinfo("너를 위한 응원", message)
    root.destroy()
root = tk.Tk()
root.withdraw()
show_message()
root.mainloop()