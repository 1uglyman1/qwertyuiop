import subprocess

# 启动程序并获取标准输入流
process = subprocess.Popen(
    "test.exe",
    stdin=subprocess.PIPE,
    text=True
)

# 向标准输入写入参数并关闭输入流
process.stdin.write("http://192.168.153.1/kodbox/#user/login")
process.stdin.close()

# 等待程序执行完毕并获取返回码
return_code = process.wait()
print(f"程序返回码: {return_code}")
