import subprocess
import cmd
import platform  # 新增：导入platform模块（之前漏了）
# 替换readline为pyreadline3（Windows专属补全库）
try:
    import pyreadline3 as readline
except ImportError:
    # 如果没装pyreadline3，跳过补全功能，不影响核心运行
    readline = None
    print("提示:未安装pyreadline3,Tab补全功能不可用,可执行 pip install pyreadline3 安装")

# 导入独立配置文件中的指令映射和补全列表
from config.cmd_mapping import COMMAND_MAP, COMPLETE_COMMANDS

# 补全功能实现（仅当readline可用时生效）
if readline:
    def completer(text, state):
        matches = [cmd for cmd in COMPLETE_COMMANDS if cmd.startswith(text)]
        if state < len(matches):
            return matches[state]
        else:
            return None

    # 绑定补全规则
    readline.set_completer(completer)
    readline.parse_and_bind('tab: complete')

# 核心业务逻辑
class ChineseCMD(cmd.Cmd):
    prompt = "中文CMD > "
    intro = "欢迎使用中文CMD!输入「帮助」查看所有指令\n"

    def default(self, line):
        line = line.strip()
        
        # 帮助指令
        if line == "帮助":
            print("===== 中文CMD指令列表 =====")
            for cn_cmd, sys_cmd in COMMAND_MAP.items():
                print(f"{cn_cmd} → {sys_cmd}")
            print("==========================")
            return
        
        # 退出指令
        if line == "退出":
            print("再见！")
            return True
        
        # 解析指令和参数
        cmd_parts = line.split(maxsplit=1)
        cn_cmd = cmd_parts[0]
        args = cmd_parts[1] if len(cmd_parts) > 1 else ""

        # 执行系统指令
        # 如果输入的中文指令在映射表中，执行对应的系统命令
        if cn_cmd in COMMAND_MAP:
            sys_cmd = f"{COMMAND_MAP[cn_cmd]} {args}".strip()
            try:
                result = subprocess.run(
                    sys_cmd,
                    shell=True,
                    capture_output=True,
                    # 编码设置根据操作系统自动调整，确保输出正确显示中文
                    encoding="gbk" if platform.system() == "Windows" else "utf-8"
                )
                if result.stdout:
                    print(result.stdout)
                if result.stderr:
                    print(f"错误：{result.stderr}")
            except Exception as e:
                print(f"执行失败：{str(e)}")
        # 如果输入的指令不在映射表中，提示用户输入帮助查看支持的指令
        else:
            print(f"未识别指令「{line}」，输入「帮助」查看所有支持的指令")

if __name__ == "__main__":
    ChineseCMD().cmdloop()