import tkinter as tk
import os

def shutdown():
    time = entry.get()  # 获取输入的时间（单位：分钟）
    os.system(f'shutdown -s -t {int(time) * 60}')  # 执行关机命令

# 创建窗口
window = tk.Tk()
window.title("定时关机")
window.geometry("300x150")

# 创建标签
label = tk.Label(window, text="请输入关机时间（分钟）:")
label.pack()

# 创建输入框
entry = tk.Entry(window)
entry.pack()

# 创建按钮
button = tk.Button(window, text="关机", command=shutdown)
button.pack()

# 进入主循环
window.mainloop()
