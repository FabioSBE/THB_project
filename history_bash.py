c_dict_all = {}
c_dict_most = {}
c_dict_search = {}
lista_final = []

#Receives a list and inserts the items in dictionary['keys'] and counts their occurrences in dictionary['value']
def cont_commands(lf):
    for line in lf:
        line = line.rstrip()
        if line[7:].startswith('sudo'):
            c_dict_all[line[12:]] = c_dict_all.get(line[12:], 0) + 1    
        else:
            c_dict_all[line[7:]] = c_dict_all.get(line[7:], 0) + 1
    return dict(reversed(sorted(c_dict_all.items(), key=lambda item: item[1])))
                
#Takes the txt files and an empty list as parameters and returns a list where each item corresponds to a line in the file and excluding repetitions between the input files.
def segrecacao(f1):
    listaf1 = []
    for line in f1:
        line = line.rstrip()
        listaf1.append(line)
    for v in listaf1:
        if v not in lista_final:
            lista_final.append(v)
    
#User enters command to be searched
def busca_comandos(cl):
    lista = {}
    comando = input("\nType a command: ")
    for x,y in cl.items():
        if x.startswith(comando):
            lista[x] = lista.get(x,y)
                        
    return dict(reversed(sorted(lista.items(), key=lambda item: item[1])))

#Rank the main commands used by the user
def comad_principais(lista_final):
    command_princ = {}
    for x in lista_final:
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
            segrecacao(open(a))
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
        c_dict_all = cont_commands(lista_final)
    elif loop == '2':
        print (c_dict_all, '\n')
    elif loop == '3':
        c_dict_most = comad_principais(lista_final)
        print (c_dict_most, '\n')
    elif loop == '4':
        c_dict_search = busca_comandos(c_dict_all)
        print (c_dict_search, '\n')
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