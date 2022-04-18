import pytesseract as tess
import  cv2
import numpy as np
import pandas as  pd
import urllib.request
from PIL import Image


def remove(string):
    string = string.replace(" ", "")
    string = string.replace("|", "")
    return string.replace("\n", "")

def get_str_btw(s, f, b):
    par = s.partition(f)
    return (par[2].partition(b))[0][:]

def get_str_btw1(s, f):
    par = s.partition(f)
    return par[2][0:18]


path1 = r'C:\OCR\.'
data_1 = pd.read_excel(path1)
data_1.insert(data_1.shape[1], '姓名1','')
data_1.insert(data_1.shape[1], '采集时间','')
data_1.insert(data_1.shape[1], '检测时间','')
list1 = []
list2 = []
N = data_1.shape[0]
for i in range(0,N):
    list1.append(i)
    print(i)
    if data_1.iloc[i][2] == '是':
        list2.append(i)
        path2 = data_1.iloc[i][3]
        resp = urllib.request.urlopen(path2)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        text = tess.image_to_string(image, lang="chi_sim")
        # text = tess.image_to_string(image, lang='chi_sim_vert')
        # print(text)
        text1 = remove(text)
        # print(text1)
        text1 = text1.replace(text1[-20:-1],'')
        nameifo = get_str_btw(text1,'姓名','身份')
        time1 = get_str_btw1(text1,'检测时间')
        time2= get_str_btw1(text1,'采集时间')
        data_1.loc[i,'姓名1'] = nameifo
        data_1.loc[i,'检测时间'] = time1
        data_1.loc[i,'采集时间'] = time2



outputpath=r'C:\OCR\.'
data_1.to_excel(outputpath,index=False,header=True)















