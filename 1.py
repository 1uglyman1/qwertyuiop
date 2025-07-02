import subprocess
import time
import pyautogui

# 启动程序
subprocess.Popen("test.exe")

# 等待程序启动（根据实际情况调整等待时间）
time.sleep(2)

# 输入参数
pyautogui.typewrite("your_parameter_here")

# 按下回车键确认
pyautogui.press("enter")