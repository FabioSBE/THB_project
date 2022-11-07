command_list = {}
lista_final = []
a = {}

#Recebe uma lista e insere os itens em dicionário['keys'] e conta suas ocorrências em
#dicionário['value']
def cont_commands(lf):
    for line in lf:
        line = line.rstrip()
        if line[7:].startswith('sudo'):
            command_list[line[12:]] = command_list.get(line[12:], 0) + 1    
        else:
            command_list[line[7:]] = command_list.get(line[7:], 0) + 1
    return dict(reversed(sorted(command_list.items(), key=lambda item: item[1])))
                
#Recebe os arquivos txt e um lista vazia como parâmetros e retorna uma lista
#onde cada item corresponde a uma linha do arquivo e excluindo repetições entre os arquivos do input.  
def segrecacao(f1):
    listaf1 = []
    for line in f1:
        line = line.rstrip()
        listaf1.append(line)
    for v in listaf1:
        if v not in lista_final:
            lista_final.append(v)
    

#Usuário insere comando a ser pesquisado
def busca_comandos(cl):
    lista = {}
    comando = input("\nType a command: ")
    for x,y in cl.items():
        if x.startswith(comando):
            lista[x] = lista.get(x,y)
                        
    return dict(reversed(sorted(lista.items(), key=lambda item: item[1])))

#Ranqueia os principais comandos utilizados pelo usuário
def comad_principais(lista_final):
    command_princ = {}
    for x in lista_final:
        x = x.rsplit()
        if x[1] == 'sudo':
            command_princ[x[2]] = command_princ.get(x[2], 0) + 1
        else:
            command_princ[x[1]] = command_princ.get(x[1], 0) + 1
    
    return (dict(reversed(sorted(command_princ.items(), key=lambda item: item[1]))))

def import_files():
    finput = input("\nDigite o nome do arquivo contendo a lista geral: ")
    try:
        fhist01 = open(finput)
        for a in fhist01:
            a = a.rstrip()
            segrecacao(open(a))
        print ('\nLoading is Complete!!\n')
    except:
        print ("\nArquivo não encontrado!!!\n")
    return finput

def menu(l):
    for a in open('menu.txt'):
        a = a.rstrip()
        print (a)
    l = input ("\nSelect one option to go: ")
    return l
    
#Main
loop = None
while loop != '5':
    loop = menu(loop)
    if loop == '1':
        import_files()
        cont_commands(lista_final)
    elif loop == '2':
        print (cont_commands(lista_final))
    elif loop == '3':
        a = comad_principais(lista_final)
        print (a)
    elif loop == '4':
        print (busca_comandos(command_list))
    
    
        





#indices = int(comparar_juntar(fhist01, fhist02, fhist03))
#print (type(indices))
#uniao_arquivo(fhist01, indices)
#uniao_arquivo(fhist02, indices)
#uniao_arquivo(fhist03, indices)

#def conta_dicio(diciona):
#    comando = input("Comando: ")
#    for line in diciona.keys():
#        if 


    #for words in line:
    #    print (words)

#def gravar_arquivos (dicionario):
#    fteste = open(foutput, 'w')
#    fcommand = input("\nType a command: ")
#    for line in fhand:
#        line = line.rstrip()
#        if line[7:].startswith(fcommand):
#            fteste.write(line)
#            fteste.write('\n')




#cont_commands(fhist01)
#print (command_list)