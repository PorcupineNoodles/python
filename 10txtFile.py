
def creatfile():
    import os
    #加载系统模块
    fileNum = input("创建几个文件：")
    #自定义创建文件个数
    filePath = 'e:\\python\\'
    #自定义创建路径
    for count in range(1,int(fileNum)+1):
    #循环不包含最后一个数字，须加1
        filename = str(count)
        #定义文件名前缀
        file = open(filePath + filename + ".txt" , 'w')
        #创建并打开文件
        file.close()
        #关闭文件
    if int(fileNum) < 1:
        print("无文件创建")
    #当无文件创建时打印内容
    else:
        print("已创建{}个文件".format(fileNum))
creatfile()