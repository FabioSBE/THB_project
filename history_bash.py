fhist01 = open ('ubuntu_history.txt')
fhist02 = open ('h_bash.txt')
fhist03 = open ('bash_h_ul.txt')
command_list = {}
lista_final = []

#Recebe uma lista e insere os itens em dicionário['keys'] e conta suas ocorrências em
#dicionário['value']
def cont_commands(lf):
    for line in lf:
        line = line.rstrip()
        if line[7:].startswith('sudo'):
            command_list[line[11:]] = command_list.get(line[11:], 0) + 1    
        else:
            command_list[line[7:]] = command_list.get(line[7:], 0) + 1
                
#Receber os arquivos txt como parâmetros e a lista vazia e retorna uma lista
#onde cada item corresponde a uma linha do arquivo e excluindo repetições.  
def outra_maneira(f1,f2,f3,lf):
    listaf1 = []
    listaf2 = []
    listaf3 = []
    for line in f1:
        line = line.rstrip()
        listaf1.append(line)
    for line in f2:
        line = line.rstrip()
        listaf2.append(line)
    for line in f3:
        line = line.rstrip()
        listaf3.append(line)

    for v in listaf1:
        if v not in lf:
            lf.append(v)
    for v in listaf2:
        if v not in lf:
            lf.append(v)
    for v in listaf3:
        if v not in lf:
            lf.append(v)
    return (lf)

#Usuário insere comando a ser pesquisado
def busca_comandos(cl):
    lista = {}
    comando = input("Digite um comando: ")
    for x,y in cl.items():
        if x.startswith(comando):
            lista[x] = lista.get(x,y)
                        
    print (dict(reversed(sorted(lista.items(), key=lambda item: item[1]))))
    

lista_final = outra_maneira(fhist01,fhist02,fhist03,lista_final)
cont_commands(lista_final)
#print (command_list.items())
#print (dict(sorted(command_list.items(), key=lambda item: item[1])))

busca_comandos(command_list)
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