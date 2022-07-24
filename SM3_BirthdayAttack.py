from pysmx.SM3 import SM3
#本题已预先安装了相关环境
#SM3安装环境相关参考链接见小组repo里面的README(Siyu Chen)文件
#SM3具体实现代码为C++语言编写，见小组SM3_Implement.cpp文件，该文件作者为陈思宇（Siyu Chen）
import math
import random
func=SM3()
List1=[]
List2=[]
def Birthday_Attack(n):#实现SM3生日攻击的前n位碰撞
    for i in range(2**n):
        a1=random.randint(0,2**n)#随机生成大整数a1和a2
        a2=random.randint(0,2**n)
        b1=str(a1)#转换为字符串形式，以便于满足SM3函数要求
        b2=str(a2)
        func.update(b1)
        i=func.hexdigest()
        List1.append(i)
        func.update(b2)
        j=func.hexdigest()
        List2.append(j)
        char1=List1[0][0:n]#对SM3得到的结果进行前n位切片分别用char1和char2表示
        char2=List2[0][0:n]
        if(char1==char2):
            print("攻击成功")
            break
        else:
            print("攻击失败")
Birthday_Attack(16)#可根据需要将函数变量n改为任何整数
