import history_bash as a

final_list = []

loop = None
while loop != '6':
    loop = a.menu(loop)
    if loop == '1':
        final_list = a.import_files()
        c_dict_all = a.cont_com(final_list)
    elif loop == '2':
        for x,y in c_dict_all.items():
            print (x, ' - ', y)
    elif loop == '3':
        c_dict_most = a.main_com(final_list)
        for x,y in c_dict_most.items():
            print (x, ' - ', y)
    elif loop == '4':
        c_dict_search = a.search_com(c_dict_all)
        for x,y in c_dict_search.items():
            print (x, ' - ', y)
    elif loop == '5':
        for x in open('./menus/menu_save.txt'):
            x = x.rstrip()
            print (x)
        c_dict_chose = input ("\nSelect one option to go: ")
        if c_dict_chose == '1':
            a.output_files(c_dict_all)
        elif c_dict_chose == '2':
            a.output_files(c_dict_most)
        elif c_dict_chose == '3':
            a.output_files(c_dict_search)