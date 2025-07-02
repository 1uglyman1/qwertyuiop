import subprocess
import os

# 设置UTF-8环境变量
env = os.environ.copy()
env["PYTHONIOENCODING"] = "utf-8"
env["PYTHONUTF8"] = "1"

try:
    # 执行test.exe并捕获输出
    result = subprocess.run(
        "test.exe",
        input="http://www.xfyun.cn",
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",  # 替换无法编码的字符
        env=env,
        check=True  # 检查返回状态码
    )
    
    print("Standard Output:")
    print(result.stdout)
    
    print("\nStandard Error:")
    print(result.stderr)
    
    print(f"\nReturn Code: {result.returncode}")
    
except subprocess.CalledProcessError as e:
    # 错误处理：完全使用ASCII字符
    print("Execution failed: Command '{}' returned non-zero exit status {}".format(
        e.cmd, e.returncode))
    
    # 安全打印输出信息
    if e.stdout:
        print("\nStandard Output:")
        print(e.stdout.encode('utf-8', errors='replace').decode('utf-8'))
    
    if e.stderr:
        print("\nStandard Error:")
        print(e.stderr.encode('utf-8', errors='replace').decode('utf-8'))
    
    # 尝试确定test.exe路径
    try:
        which_result = subprocess.run(
            ["where", "test.exe"],
            capture_output=True,
            text=True,
            env=env
        )
        if which_result.returncode == 0:
            print(f"\ntest.exe location: {which_result.stdout.strip()}")
        else:
            print("\ntest.exe not found in PATH")
    except Exception as ex:
        print(f"\nError checking test.exe location: {str(ex)}")
    
except Exception as e:
    # 捕获其他异常
    print("An unexpected error occurred: " + str(e).encode('utf-8', errors='replace').decode('utf-8'))
