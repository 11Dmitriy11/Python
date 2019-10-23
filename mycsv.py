def read_csv(path_to_csv_file, del_= ','):
     with open(path_to_csv_file, 'r') as file_:
        List = [[n.rstrip('\n') for n in x.split(del_)] for x in file_.readlines()]
     return(List)


         

