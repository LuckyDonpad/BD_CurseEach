import glob
import os
import ftplib
from time import sleep

host = "<Host>"
ftp_user = "<User>"
ftp_password = "<Password>"
ftp = ftplib.FTP(host, ftp_user, ftp_password)


def find_latest_dump():
    list_of_files = glob.glob(r'CRM\backups/*')  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


while True:
    os.system("start /wait cmd /c python manage.py dbbackup")
    sleep(10)
    file = find_latest_dump()
    file_to_upload = open(file, 'rb')
    ftp.storbinary('STOR ' + file, file_to_upload)
    sleep(60 * 60)
