#字符编码作业
with open(r'C:\Users\admin\Desktop\python进阶测试-作业1-字符编码集-task07\cfiles\utf8编码.txt','r',encoding='utf8') as f1:
    s1=f1.read()
    f1.close()
with open(r'C:\Users\admin\Desktop\python进阶测试-作业1-字符编码集-task07\cfiles\gbk编码.txt','r',encoding='gbk') as f2:
    s2=f2.read()
    f2.close()
s3=s1+s2
print(s3)
newfilename=input('请输入新文件的名称：')

with open(f'F:/{newfilename}.txt','w',encoding='utf8') as f3:
    f3.write(s3)

