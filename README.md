# 网络设备Ping状态监控脚本

这是一个用 Python 编写的定时 Ping 工具，适用于网络运维场景。可用于自动检测网络设备是否在线，记录响应时间，并生成日志与报表。

## 📌 功能

- 定时 ping 多个 IP
- 记录每次检测结果到 `ping_log.txt`
- 输出当前所有 IP 状态报告 `ping_report.csv`

## ⚙️ 使用方法

1. 修改脚本中的配置：

```python
IP_LIST = ['192.168.111.171', '202.96.134.133', '192.168.111.254']
INTERVAL = 60  # 检测间隔（单位：秒）
运行脚本：
python ping_monitor.py
输出文件：

ping_log.txt: 每次检测日志（自动生成）

ping_report.csv: 最后状态报告（自动生成）

💻 环境要求
Python 3.x

使用标准库，无需安装第三方库

🗂️ 项目结构
ping_monitor.py       # 主程序脚本
README.md             # 项目说明文件
ping_log.txt          # 日志输出（运行后自动生成）
ping_report.csv       # 状态报告（运行后自动生成）
📎 编写者：andy

时间：2025.6