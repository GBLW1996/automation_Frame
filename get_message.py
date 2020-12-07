import re
import os
import clr
from certificateDll import *
#tu1 = os.walk(r"C:\Users\Administrator\Downloads")
clr.AddReference('certificateDll')
certificate_information = certificate.getCert(r"D:\bin\QQScLauncher.exe")
certificate_information = str(certificate_information)
digital_signature = re.findall(r'CN=.+C=CN', certificate_information)
digital_moment = digital_signature[0]
digital_signature_data = str(digital_moment[3:-6])
# digital_signature_data数字签名
timestamp = re.findall(r'signDate.+', certificate_information)
timestamp_moment = timestamp[0]
timestamp_data = str(timestamp_moment[11:-2])
# timestamp_data时间戳
# for root, dirs, files in os.walk(r"C:\Users\Administrator\Downloads"):
#     print(root) #当前目录路径
#     print(dirs) #当前路径下所有子目录
#     print(files) #当前路径下所有非目录子文件
print(timestamp_data)