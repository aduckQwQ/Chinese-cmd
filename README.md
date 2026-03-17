<!--
 * @Author: aduckQwQ 2294036359@qq.com
 * @Date: 2026-03-14 20:22:53
 * @LastEditors: aduckQwQ 2294036359@qq.com
 * @LastEditTime: 2026-03-14 20:37:13
 * @FilePath: \GitHub Project\Chinese cmd\README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
#Chinese cmd
中文 CMD (Chinese-cmd)
一个纯后端实现的中文命令行工具，支持将中文指令映射为系统原生命令。
功能介绍
支持将中文指令转换为 Windows 系统命令
纯 Python 实现，无需额外依赖
可自定义指令映射，扩展方便
运行步骤
安装 Python 3.6+ 版本
（可选）安装中文输入补全库：
bash
运行
pip install pyreadline3
执行启动命令：
bash
运行
python main.py
输入中文指令（如 打开文件夹），工具会自动转换为对应系统命令执行
项目结构
plaintext
Chinese-cmd/
├── main.py          # 主程序入口
├── config/          # 指令映射配置目录
└── README.md        # 项目说明文档
技术说明
后端语言：Python 3
核心逻辑：中文指令解析 + 系统命令映射
兼容系统：Windows 10/11