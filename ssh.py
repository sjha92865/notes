# # import os

# # c=os.system("ssh shubham_2213@10.87.3.236")
# # unknown_dir = os.system("cd doesnotexist")
# # # print(c)
# import sys
# sys.stderr = open('/dev/null')       # Silence silly warnings from paramiko
# import paramiko as pm
# sys.stderr = sys.__stderr__
# import os

# HOST = '10.87.3.236'
# USER = 'shubham_2213'
# PASSWORD = ''

# client = pm.SSHClient()
# # client.load_system_host_keys()
# client.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
# client.set_missing_host_key_policy(pm.AutoAddPolicy())
# # client.set_missing_host_key_policy(AllowAllKeys())
# # client.connect(HOST, username=USER, password=PASSWORD)
# client.connect(HOST, username=USER)

# channel = client.invoke_shell()
# stdin = channel.makefile('wb')
# stdout = channel.makefile('rb')

# stdin.write('''
# sudo -i
# cd /opt
# ls
# exit
# ''')
# print(stdout.read())

# stdout.close()
# stdin.close()
# client.close()p
# import paramiko
# client=paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # com="ls ~/desktop"
# c=client.connect('10.87.3.236', username='shubham_2213')
# print(c)
# channel = client.invoke_shell()
# print()
# stdin = channel.makefile('wb')
# stdout = channel.makefile('rb')

# stdin.write('''

# ls
# exit
# ''')
# print(stdout.read())
# print(f'STDOUT: {stdout.read().decode("utf8")}')

# stdout.close()
# stdin.close()
# client.close()

from paramiko import SSHClient, AutoAddPolicy

hosts = ['10.87.3.236', 
         ]

for host in hosts:
    client = SSHClient()
    # client.load_host_keys('C:/Users/brad/.ssh/known_hosts')
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.load_system_host_keys()
    client.connect(host, username='shubham_2213')

    # Run a command (execute PHP interpreter)
    #client.exec_command('hostname')
    stdin, stdout, stderr = client.exec_command('df -h;ls;top -b -n1')

    if stdout.channel.recv_exit_status() == 0:
        print(f'STDOUT: {stdout.read().decode("utf8")}')
    else:
        print(f'STDERR: {stderr.read().decode("utf8")}')

    stdin.close()
    stdout.close()
    stderr.close()
    client.close()
