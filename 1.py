import subprocess
import os

# 设置UTF-8环境变量
env = os.environ.copy()
env["PYTHONIOENCODING"] = "utf-8"
env["PYTHONUTF8"] = "1"

try:
    # 执行test.exe
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
    
    # 将输出保存到文件
    with open("test_output.txt", "w", encoding="utf-8") as f:
        f.write("Standard Output:\n")
        f.write(result.stdout)
        f.write("\n\nStandard Error:\n")
        f.write(result.stderr)
    
    print("test.exe executed successfully. Return code:", result.returncode)
    print("Output saved to test_output.txt")
    
except subprocess.CalledProcessError as e:
    # 纯ASCII错误消息
    error_msg = "Execution failed: Command '{}' returned non-zero exit status {}".format(
        ' '.join(e.cmd), e.returncode)
    
    # 尝试打印ASCII错误消息
    try:
        print(error_msg)
    except:
        # 如果打印失败，则使用更安全的方式
        print(error_msg.encode('ascii', errors='replace').decode('ascii'))
    
    # 保存详细错误信息到文件
    with open("error_details.txt", "w", encoding="utf-8") as f:
        f.write(error_msg + "\n\n")
        if e.stdout:
            f.write("Standard Output:\n" + e.stdout)
        if e.stderr:
            f.write("\n\nStandard Error:\n" + e.stderr)
    
    print("Error details saved to error_details.txt")
    
except Exception as ex:
    # 确保异常消息安全输出
    safe_msg = str(ex).encode('ascii', errors='replace').decode('ascii')
    print("Unexpected error occurred:", safe_msg)
