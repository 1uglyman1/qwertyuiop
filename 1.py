import subprocess
import sys
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
process = subprocess.Popen(
    "test.exe",
    stdin=subprocess.PIPE,
    text=True
)
process.stdin.write("http://www.xfyun.cn")
process.stdin.close()
return_code = process.wait()
print(f"ret_code: {return_code}")
