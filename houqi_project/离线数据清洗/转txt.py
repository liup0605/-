import os
from win32com import client
rootdir = 'E:\python\lixianshuju\word'
list1 = os.listdir(rootdir)
# print(list1)
# length = len(list1)
# print(length)
for i in list1:
    print(i)
    try:
        word = client.Dispatch('Word.Application')
        path = r'E:\python\lixianshuju\word\%s'%i
        doc = word.Documents.Open(path)  # 目标路径下的文件
        doc.SaveAs(r'E:\python\lixianshuju\word1\%s.txt'%i.replace('.doc',''), 4)
        doc.Close()
        word.Quit()
    except:
        print('无效')