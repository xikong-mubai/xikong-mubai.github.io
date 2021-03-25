import os
pwd = os.getcwd()
i1=0
files = os.listdir(pwd)
files_time = []
for i in files:
    files_time.append([i,os.path.getctime(i)])
tmp = []
while len(files_time) != 0:
    tmp_file = ['',0]
    for i in files_time:
        if tmp_file[1] < i[1]:
            tmp_file = i
    files_time.remove(tmp_file)
    tmp.append(tmp_file[0])

for i in tmp[::-1]:
    os.rename(i,str(i1)+'.tmp.'+i.split('.')[1])
    i1+=1
for i in os.listdir(pwd):
    i_tmp = i.replace('.tmp','')
    os.rename(i,i_tmp)
