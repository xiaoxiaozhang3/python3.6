import  re
def read_html(path):
    with open(path,"r",encoding="utf-8") as f :
        return f.read()

def write_html(path,str1):
    with open(path,"a",encoding="utf-8") as f1:
        f1.write(str1)

if __name__ == '__main__':
    path = r"E:\pycharm\zuoye\qiushibaike.htm"
    path1 = r"E:\pycharm\zuoye\venv"
    str1 = read_html(path)
    # chinese_list = re.findall(r'<div class="content">(.*?)</span>',str1,flags=re.DOTALL+re.MULTILINE)
    # # chinese_str = str(chinese_list)
    # str3 =''
    # for x in chinese_list:
    #     y = re.findall(r'\n\n\n(.*)\n',x,flags=re.DOTALL+re.MULTILINE)
    #     # y = re.findall(r'[<br>]',y[0],flags=re.DOTALL+re.MULTILINE)
    #     for z in y:
    #         str3 += str(z)

    # write_html(r"E:\pycharm\zuoye\新建文本文档.txt",str3)
    # print(str3)
    str2 = re.findall(r'<span>\n\n\n(.*)\n\n</span>',str1)
    for x in str2:
        x += "\n"
        write_html("test.txt",x)
