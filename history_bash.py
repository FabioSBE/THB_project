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
                
#Recebe os arquivos txt e um lista vazia como parâmetros e retorna uma lista
#onde cada item corresponde a uma linha do arquivo e excluindo repetições entre os arquivos do input.  
def segracacao(f1):
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
    comando = input("Digite um comando: ")
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
    
#Main
print ("\n================================================================\n* Bem vindo ao resumo do history bash do seu terminal linux!!! *\n================================================================\n")
finput = None
while finput != 'n':
    finput = input("\nDigite o nome do arquivo com os dados salvos do seu history\n(digite 'n' se quiser parar de ler arquivos): ")
    if finput != 'n':
        try:
            fhist01 = open(finput)
            segracacao(fhist01)
        except:
            print ("\nArquivo não encontrado!!!")
                    
cont_commands(lista_final)
print (sum(command_list.values()))
a = comad_principais(lista_final)
print (a)

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