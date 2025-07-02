import subprocess
import os
import sys

# 确保所有输出都使用UTF-8编码
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# 设置环境变量
env = os.environ.copy()
env["PYTHONIOENCODING"] = "utf-8"
env["PYTHONUTF8"] = "1"

# 尝试查找test.exe的位置
def find_test_exe():
    """尝试定位test.exe的位置"""
    # 检查当前目录
    if os.path.exists("test.exe"):
        return os.path.abspath("test.exe")
    
    # 检查系统路径
    for path in os.environ["PATH"].split(os.pathsep):
        exe_path = os.path.join(path, "test.exe")
        if os.path.exists(exe_path):
            return exe_path
    
    # 尝试使用where命令(GitHub Actions Windows环境)
    try:
        result = subprocess.run(
            ["where", "test.exe"],
            capture_output=True,
            text=True,
            env=env
        )
        if result.returncode == 0:
            return result.stdout.strip().splitlines()[0]
    except:
        pass
    
    return None

# 查找test.exe
test_exe_path = find_test_exe()

if test_exe_path is None:
    print("[ERROR] 无法找到 test.exe!")
    print("[INFO] 当前目录内容:")
    for item in os.listdir('.'):
        print(f"  - {item}")
    print("[INFO] 系统PATH环境变量:")
    for path in os.environ["PATH"].split(os.pathsep):
        print(f"  - {path}")
    sys.exit(1)

print(f"[INFO] 找到 test.exe: {test_exe_path}")

try:
    print("[INFO] 开始执行 test.exe...")
    
    # 使用完整路径执行程序
    result = subprocess.run(
        [test_exe_path],
        input="http://www.xfyun.cn",
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="backslashreplace",
        env=env,
        check=True
    )
    
    # 保存输出到文件
    with open("test_output.txt", "w", encoding="utf-8") as f:
        f.write("=== 标准输出 ===\n")
        f.write(result.stdout)
        f.write("\n\n=== 错误输出 ===\n")
        f.write(result.stderr)
    
    print(f"[INFO] test.exe 执行成功，返回代码: {result.returncode}")
    print("[INFO] 输出已保存到 test_output.txt")
    
except subprocess.CalledProcessError as e:
    # 保存详细错误信息到文件
    with open("error_details.txt", "w", encoding="utf-8") as f:
        f.write(f"命令执行失败: {' '.join(e.cmd)}\n")
        f.write(f"返回代码: {e.returncode}\n\n")
        f.write("=== 标准输出 ===\n")
        if e.stdout:
            f.write(e.stdout)
        f.write("\n\n=== 错误输出 ===\n")
        if e.stderr:
            f.write(e.stderr)
    
    # 打印安全的错误信息
    safe_cmd = ' '.join(e.cmd).encode('ascii', 'replace').decode('ascii')
    print(f"[ERROR] 命令执行失败: {safe_cmd}")
    print(f"[ERROR] 返回代码: {e.returncode}")
    print("[ERROR] 详细信息已保存到 error_details.txt")
    
    # 退出脚本并返回相同的错误码
    sys.exit(e.returncode)
    
except Exception as ex:
    # 捕获其他异常并保存到日志
    error_msg = f"发生未知错误: {str(ex)}"
    with open("fatal_error.log", "w", encoding="utf-8") as f:
        f.write(error_msg)
    
    print("[CRITICAL] 发生未知错误，详情见 fatal_error.log")
    sys.exit(1)
