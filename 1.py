import subprocess
import os

# 设置环境变量确保UTF-8编码
env = os.environ.copy()
env["PYTHONIOENCODING"] = "utf-8"
env["PYTHONUTF8"] = "1"

try:
    # 使用subprocess.run替代Popen，简化操作
    result = subprocess.run(
        "test.exe",
        input="http://www.xfyun.cn",
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
        check=True
    )
    
    # 确保输出正确编码
    print("Output:", result.stdout.encode('utf-8', errors='replace').decode('utf-8'))
    print("Errors:", result.stderr.encode('utf-8', errors='replace').decode('utf-8'))
    print(f"ret_code: {result.returncode}")
    
except subprocess.CalledProcessError as e:
    # 打印详细的错误信息，避免直接打印包含Unicode的字符串
    print("执行失败: Command '{}' returned non-zero exit status {}".format(
        e.cmd, e.returncode))
    
    # 安全地打印输出和错误信息
    if e.stdout:
        print("标准输出:", e.stdout.encode('utf-8', errors='replace').decode('utf-8'))
    if e.stderr:
        print("错误输出:", e.stderr.encode('utf-8', errors='replace').decode('utf-8'))
    
    # 尝试获取test.exe的完整路径（用于调试）
    try:
        which_result = subprocess.run(
            ["where", "test.exe"], 
            capture_output=True, 
            text=True,
            env=env
        )
        print(f"test.exe 路径: {which_result.stdout.strip()}")
    except:
        print("无法确定test.exe路径")
    
except Exception as e:
    # 捕获其他异常，避免使用Unicode字符
    print("发生未知错误:", str(e).encode('utf-8', errors='replace').decode('utf-8'))
