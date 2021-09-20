a=int(input("输入要选择的图片数量（起点）"))
b=int(input("输入要选择的图片数量（终点）"))
c=input("输入图片后缀")
b=b+1
for i in range(b-a):
    print('<img src="Pictures/%d%s" alt="这个图片没了">'%(a,c))
    a+=1
import time
time.sleep(1000)
