import subprocess
process = subprocess.Popen(
    "test.exe",
    stdin=subprocess.PIPE,
    text=True
)
process.stdin.write("http://www.xfyun.cn")
process.stdin.close()
return_code = process.wait()
print(f"ret_code: {return_code}")
