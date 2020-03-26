import os
pwd = os.getcwd()
i1=0
for i in os.listdir(pwd):
    os.rename(i,str(i1)+'.tmp.'+i.split('.')[1])
    i1+=1
for i in os.listdir(pwd):
    i_tmp = i.replace('.tmp','')
    os.rename(i,i_tmp)
