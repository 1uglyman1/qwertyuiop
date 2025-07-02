import subprocess
import os

# Optional: set environment variable for UTF-8
env = os.environ.copy()
env["PYTHONIOENCODING"] = "utf-8"

process = subprocess.Popen(
    "test.exe",
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    env=env
)
output, errors = process.communicate("http://www.xfyun.cn")
print("Output:", output)
print("Errors:", errors)
ret_code = process.returncode
print(f"ret_code: {ret_code}")
