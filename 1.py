import subprocess
import os

# 设置环境变量确保UTF-8编码
env = os.environ.copy()
env["PYTHONIOENCODING"] = "utf-8"
env["PYTHONUTF8"] = "1"

try:
    # 执行test.exe并捕获输出，但不尝试打印
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
    
    # 将输出保存到文件而不是打印到控制台
    with open("test_output.txt", "w", encoding="utf-8") as f:
        f.write("Standard Output:\n")
        f.write(result.stdout)
        f.write("\n\nStandard Error:\n")
        f.write(result.stderr)
    
    print(f"test.exe 执行成功，返回代码: {result.returncode}")
    print("输出已保存到 test_output.txt")
    
except subprocess.CalledProcessError as e:
    # 不尝试打印可能包含非ASCII字符的输出
    print(f"执行失败: Command '{' '.join(e.cmd)}' 返回非零状态码 {e.returncode}")
    
    # 将错误信息保存到文件
    with open("error_details.txt", "w", encoding="utf-8") as f:
        f.write(f"执行失败: Command '{' '.join(e.cmd)}' 返回非零状态码 {e.returncode}\n\n")
        if e.stdout:
            f.write("标准输出:\n")
            f.write(e.stdout)
        if e.stderr:
            f.write("\n\n标准错误:\n")
            f.write(e.stderr)
    
    print("错误详情已保存到 error_details.txt")
    
except Exception as ex:
    print(f"发生未知错误: {str(ex)}")
