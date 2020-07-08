import psutil
import os
import time
import mailSender


def process_display(log_dir="dj"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except Exception as e:
            print("Error at file dir : ", e)
    separator = "_" * 80
    unique_file_name = "%s.log" % time.ctime().replace(':', "_")
    log_path = os.path.join(log_dir, unique_file_name)
    file = open(log_path, 'w')
    file.write(separator + "\n")
    file.write("Process Loges: " + time.ctime() + "\n")
    file.write(separator + "\n")
    file.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)

            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        file.write("%s\n" % element)

    print(" log File Successfully Generated at location : %s" % log_path)

    try:
        connected = mailSender.is_connected()

        if connected:
            mailSender.mail_sender(log_path, time.ctime())
        else:
            print("there is no internet connection")
    except Exception as E:
        print("invalid:", E)
