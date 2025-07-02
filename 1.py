import subprocess
import os

# 设置环境变量确保UTF-8编码
env = os.environ.copy()
env["PYTHONIOENCODING"] = "utf-8"
env["PYTHONUTF8"] = "1"  # 确保Python 3使用UTF-8

try:
    # 使用subprocess.run替代Popen，简化操作
    result = subprocess.run(
        "test.exe",
        input="http://www.xfyun.cn",
        capture_output=True,
        text=True,
        encoding="utf-8",  # 显式指定编码
        errors="replace",  # 替换无法编码的字符
        env=env,
        check=True  # 如果返回非零状态码，抛出异常
    )
    
    print("Output:", result.stdout)
    print("Errors:", result.stderr)
    print(f"ret_code: {result.returncode}")
    
except subprocess.CalledProcessError as e:
    print(f"执行失败: {e}")
    print("标准输出:", e.stdout)
    print("错误输出:", e.stderr)
except Exception as e:
    print(f"发生未知错误: {e}")
