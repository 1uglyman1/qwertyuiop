import subprocess
import os
import sys
import io

# 设置环境变量确保UTF-8编码
env = os.environ.copy()
env["PYTHONIOENCODING"] = "utf-8"
env["PYTHONUTF8"] = "1"

# 强制标准输出使用UTF-8编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

try:
    # 使用subprocess.run替代Popen，简化操作
    result = subprocess.run(
        "test.exe",
        input="http://",
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",  # 替换无法编码的字符
        env=env,
        check=True  # 如果返回非零状态码，抛出异常
    )
    
    # 确保输出正确编码
    print("Output:", result.stdout)
    print("Errors:", result.stderr)
    print(f"ret_code: {result.returncode}")
    
except subprocess.CalledProcessError as e:
    # 使用ASCII字符输出错误信息，避免编码问题
    print("Execution failed: Command '{}' returned non-zero exit status {}".format(
        e.cmd, e.returncode))
    
    # 安全地打印输出和错误信息
    if e.stdout:
        print("Standard Output:", e.stdout)
    if e.stderr:
        print("Standard Error:", e.stderr)
    
    # 尝试获取test.exe的完整路径（用于调试）
    try:
        which_result = subprocess.run(
            ["where", "test.exe"], 
            capture_output=True, 
            text=True,
            env=env
        )
        print(f"test.exe location: {which_result.stdout.strip()}")
    except:
        print("Failed to determine test.exe location")
    
except Exception as ex:
    # 捕获其他异常，确保错误信息能安全输出
    print("Unexpected error:", str(ex).encode('utf-8', errors='replace').decode('utf-8'))
