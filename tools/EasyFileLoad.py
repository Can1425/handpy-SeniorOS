import os
import subprocess

def upload_directory_to_device(local_dir, device_port):
    """将本地目录上传到开发板的根目录"""
    try:
        subprocess.run([
            "mpremote",
            "connect",
            device_port,
            "mount",
            f"{local_dir}/.",  # 确保上传目录内的所有内容
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"上传文件时出错: {e}")

# 清除开发板内部文件
# DO NOT USE
# clear_device_filesystem()

print('> 在 Micropython 提示出现后,直接运行 import boot ')
# 上传本地目录的所有内容到开发板根目录
upload_directory_to_device("build", "/dev/ttyACM0")
