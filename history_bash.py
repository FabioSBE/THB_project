c_dict_all = {}
c_dict_most = {}
c_dict_search = {}
final_list = []

#Receives a list and inserts the items in dictionary['keys'] and counts their occurrences in dictionary['value']
def cont_com(lf):
    for line in lf:
        line = line.rstrip()
        if line[7:].startswith('sudo'):
            c_dict_all[line[12:]] = c_dict_all.get(line[12:], 0) + 1    
        else:
            c_dict_all[line[7:]] = c_dict_all.get(line[7:], 0) + 1
    return dict(reversed(sorted(c_dict_all.items(), key=lambda item: item[1])))
                
#Takes the txt files and an empty list as parameters and returns a list where each item corresponds to a line in the file and excluding repetitions between the input files.
def union_com(f1):
    listf1 = []
    for line in f1:
        line = line.rstrip()
        listf1.append(line)
    for v in listf1:
        if v not in final_list:
            final_list.append(v)
    
#User enters command to be searched
def search_com(cl):
    lista = {}
    comando = input("\nType a command: ")
    for x,y in cl.items():
        if x.startswith(comando):
            lista[x] = lista.get(x,y)
                        
    return dict(reversed(sorted(lista.items(), key=lambda item: item[1])))

#Rank the main commands used by the user
def main_com(final_list):
    command_princ = {}
    for x in final_list:
        x = x.rsplit()
        if x[1] == 'sudo':
            command_princ[x[2]] = command_princ.get(x[2], 0) + 1
        else:
            command_princ[x[1]] = command_princ.get(x[1], 0) + 1
    
    return (dict(reversed(sorted(command_princ.items(), key=lambda item: item[1]))))

#Import list of files in txt format
def import_files():
    #finput = input("\nInput the file path: ")
    try:
        fhist01 = open('files_comp.txt')
        for a in fhist01:
            a = a.rstrip()
            union_com(open(a))
        print ('\n**** Loading is Complete!! **** \n')
    except:
        print ("\nFile not found!!!\n")
    return

#Print options menu
def menu(l):
    for a in open('menu.txt'):
        a = a.rstrip()
        print (a)
    l = input ("\nSelect one option to go: ")
    return l

#Save dictionaries to files
def output_files (dicionario):
    foutput = input("\nType a file name: ")
    fteste = open(foutput, 'w')
    for x,y in dicionario.items():
        fteste.write(x)
        fteste.write(',')
        fteste.write(str(y))
        fteste.write('\n')

#Main
loop = None
while loop != '6':
    loop = menu(loop)
    if loop == '1':
        import_files()
        c_dict_all = cont_com(final_list)
    elif loop == '2':
        for x,y in c_dict_all.items():
            print (x, ' - ', y)
    elif loop == '3':
        c_dict_most = main_com(final_list)
        for x,y in c_dict_most.items():
            print (x, ' - ', y)
    elif loop == '4':
        c_dict_search = search_com(c_dict_all)
        for x,y in c_dict_search.items():
            print (x, ' - ', y)
    elif loop == '5':
        for a in open('menu_save.txt'):
            a = a.rstrip()
            print (a)
        c_dict_chose = input ("\nSelect one option to go: ")
        if c_dict_chose == '1':
            output_files(c_dict_all)
        elif c_dict_chose == '2':
            output_files(c_dict_most)
        elif c_dict_chose == '3':
            output_files(c_dict_search)