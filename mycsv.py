import functools
import random
import os.path
def read_csv(path_to_csv_file, del_= ','):
     if os.path.exists(path_to_csv_file)==False:
        print("Error,such file doesn't exist")
     with open(path_to_csv_file, 'r') as file_:
        List = file_.readlines()
        List1=[]
        for x in List:
           M=[]
           index_=0
           permition=True
           for index, value in enumerate(x):
               if value == '"':
                  permition = not(permition)
               if permition and value == del_:
                  M.append(x[index_:index])
                  index_ = index+1
           M.append(x[index_:index])
           List1+=[M]
     List1=[[n.replace('"','') for n  in x] for x in List1]
     for n in List1:
          str(n).split(del_)
     return (List1)
def write_csv(path_to_csv_file, data, del_=','):
     data1 = [del_.join(i) + '\n' for i in data]
     with open(path_to_csv_file, 'w') as f:
                 for i in  data:
                     for j in range(len(i)):
                           if j!=len(i)-1:
                              f.write(i[j]+'\t')
                           else:
                              f.write(i[j]+'\n')
          


