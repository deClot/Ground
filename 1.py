############################################
def func (list1,file_res,file_name):
    for i in range(len(list1)-1):
        for j in range(i+1,len(list1)):
            file_res.write('%3s %3s %3s - %3s %3s %3s %15.5f %7s\n'% (list1[i][0],\
                          list1[i][1],list1[i][2],list1[j][0],list1[j][1],\
                          list1[j][2],abs(float(list1[i][3])-float(list1[j][3])),file_name))
    return 0

#########################################################
#########################################################
#########################################################

file_name = input('Name of file/band: ')
file_ini=open(file_name,'r')
file_res=open(file_name+'.txt','w')

list1=[]

while(True):
    str1=file_ini.readline()
    if len(str1)==0:    #end of file_ini
        func(list1,file_res,file_name)
        break

    if str1.find('Sea',0,len(str1))!=-1:
        func(list1,file_res,file_name)
        list1=[]
        continue 

    str1=str1.split()
    if len(str1)==6:
        J,Ka,Kc,Tr,*_=str1
        str1=[J,Ka,Kc,Tr]
        list1.append(str1)

    if len(str1)==12:
        J,Ka,Kc,Tr,*_=str1
        str2=[J,Ka,Kc,Tr]
        list1.append(str2)

        *_,J,Ka,Kc,Tr,_,_=str1
        str2=[J,Ka,Kc,Tr]
        list1.append(str2)
file_ini.close()
file_res.close()
