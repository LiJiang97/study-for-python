#最好open(路径,encoding='utf-8')防止乱码 UTF-8中一个汉字占3个字节，一个英文字母占1个字节
#f.close() 关闭文件
#f.read(size=-1) 按字节读取，如果size为负数或不定义则读取全部。返回字符串类型。
#f.seek(offset,from)用来调整读取指针的位置。offset代表偏移多少个字节，from=0从文件开头开始，=1代表当前位置，=2代表末尾开始
#‘r’仅用来读取，‘w’仅写，写入会覆盖，‘a’仅写，从当前状态继续写入

#    字符串分割str.split('：',num),以：为标志进行分割，分割num次，返回字符串列表
#注意路径要两个反斜杠，转义字符

#封装重复操作

def save(li,wu,i):
    #教你怎么代替C语言中的%d
    file_name_li='li_'+str(i)+'.txt'
    file_name_wu='wu_'+str(i)+'.txt'
    li_file=open(file_name_li,'w')
    li_file.writelines(li)
    li_file.close()
    wu_file=open(file_name_wu,'w')
    wu_file.writelines(wu)
    wu_file.close()

def spl(path):
    f=open(path,encoding='utf-8')

    li=[]
    wu=[]
    i=1

    for each_line in f:
        if each_line[:3] == '---':
            save(li,wu,i)
            i=i+1
        else:
            if each_line[:1] == '李':
                li.append(each_line[2:])
            else:
                wu.append(each_line[2:])
            
    save(li,wu,i)
spl(input('请输入分割文件的路径：\n'))
