import paramiko

def remote_scp():
    host_ip = '10.X.X.X'
    remote_path = '/usr/monitor/week/巡检报告.xlsx'
    local_path = r'/usr/local/python_on/Daily_automation_linux/xunjian/巡检报告.xlsx'
    username = 'root'
    password = 'xxxx'
    t = paramiko.Transport((host_ip, 22))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    src = remote_path
    des = local_path
    sftp.get(src,des)
    t.close()


if __name__ == '__main__':
    remote_scp()