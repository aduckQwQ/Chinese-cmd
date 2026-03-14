'''
Author: aduckQwQ 2294036359@qq.com
Date: 2026-03-14 11:16:14
LastEditors: aduckQwQ 2294036359@qq.com
LastEditTime: 2026-03-14 11:23:36
FilePath: \GitHub Project\Chinese cmd\config\commands.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# config/cmd_mapping.py
import platform

# 中文指令映射表（独立配置，解耦业务逻辑）
COMMAND_MAP = {
    # 基础文件操作
    "查看文件": "dir" if platform.system() == "Windows" else "ls",
    "查看目录": "dir" if platform.system() == "Windows" else "ls -l",
    "创建文件夹": "mkdir",
    "删除文件": "del" if platform.system() == "Windows" else "rm",
    "删除文件夹": "rmdir /s /q" if platform.system() == "Windows" else "rm -rf",
    "清屏": "cls" if platform.system() == "Windows" else "clear",
    "退出": "exit",
    "查看IP": "ipconfig" if platform.system() == "Windows" else "ifconfig"
}

# 导出指令补全列表（供主程序使用）
COMPLETE_COMMANDS = list(COMMAND_MAP.keys())