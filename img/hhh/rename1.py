import os
pwd = os.getcwd()
i1=0
for i in os.listdir(pwd):
    os.rename(i,str(i1)+'.'+i.split('.')[1])
    i1+=1