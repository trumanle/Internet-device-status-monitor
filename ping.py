import subprocess
import time
import datetime

# 配置
IP_LIST = ['192.168.111.171', '202.96.134.133', '192.168.111.254']  # 你的IP列表
INTERVAL = 60  # 检查间隔（秒）
LOG_FILE = 'ping_log.txt'
REPORT_FILE = 'ping_report.csv'

def ping(ip):
    try:
        # Windows下ping命令
        output = subprocess.check_output(
            ['ping', '-n', '1', '-w', '1000', ip],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        if "TTL=" in output:
            # 提取响应时间
            time_ms = None
            for line in output.splitlines():
                if "时间=" in line or "time=" in line:
                    # 兼容中英文系统
                    time_part = line.split("时间=")[-1] if "时间=" in line else line.split("time=")[-1]
                    time_ms = int(time_part.split("ms")[0].replace("<", "").strip())
                    break
            return True, time_ms
        else:
            return False, None
    except subprocess.CalledProcessError:
        return False, None

def log_result(log_line):
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_line + '\n')

def write_report(status_dict):
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write("IP,状态,响应时间(ms),最后检测时间\n")
        for ip, info in status_dict.items():
            f.write(f"{ip},{info['status']},{info['time']},{info['last_checked']}\n")

def main():
    status_dict = {ip: {'status': '未知', 'time': '', 'last_checked': ''} for ip in IP_LIST}
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for ip in IP_LIST:
            online, resp_time = ping(ip)
            status = '在线' if online else '离线'
            status_dict[ip] = {
                'status': status,
                'time': resp_time if resp_time is not None else '',
                'last_checked': now
            }
            log_line = f"{now} | {ip} | {status} | 响应时间: {resp_time if resp_time is not None else 'N/A'} ms"
            log_result(log_line)
            print(log_line)
        write_report(status_dict)
        time.sleep(INTERVAL)

if __name__ == '__main__':
    main()