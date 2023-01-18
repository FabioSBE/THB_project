import os
# import json

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
      
#User enters command to be searched
def search_com(cl):
    lista = {}
    comando = input("\nType a command: ")
    for x,y in cl.items():
        if x.startswith(comando):
            lista[x] = lista.get(x,y)
                        
    return dict(reversed(sorted(lista.items(), key=lambda item: item[1])))

#Rank the main commands used by the user
def main_com(f2):
    command_princ = {}
    for x in f2:
        x = x.rsplit()
        try:    
            if x[1] == 'sudo':
                command_princ[x[2]] = command_princ.get(x[2], 0) + 1
            else:
                command_princ[x[1]] = command_princ.get(x[1], 0) + 1
        except:
            pass
    
    return (dict(reversed(sorted(command_princ.items(), key=lambda item: item[1]))))

#Import list of files in txt format
def import_files():
    try:
        final_set = set()
        for filename in os.listdir("./inputs/"):
            if filename.endswith(".txt"):
                with open(os.path.join("./inputs/", filename)) as file:
                    file_set = set(line.rstrip() for line in file)
                    final_set = final_set.union(file_set)
        final_list = sorted(list(final_set))
        print ("\nLoad complete!!\n")
    except:
        print ("\nFiles not found!\n")

    with open("./commands/All.txt", 'w') as ft:
        ft.writelines('\n'.join(final_list))
    
    return final_list
                
#Print options menu
def menu(l):
    for a in open('./menus/menu.txt'):
        a = a.rstrip()
        print (a)
    l = input ("\nSelect one option to go: ")
    return l

#Save dictionaries to files
def output_files (dicionario):
    path = "./outputs/"
    file_name = input("\nType a file name: ")
    with open(os.path.join(path, file_name), 'w') as fteste:
        for x,y in dicionario.items():
            fteste.write(f'{x},{y}\n')
            # json.dump(dicionario, fteste)

def print_commands(dicionario):
    for x,y in dicionario.items():
                print (x, ' - ', y)


    