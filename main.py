import history_bash as a

c_dict_all = []
c_dict_most = []

final_list = []

loop = None
while loop != '6':
    loop = a.menu(loop)
    if loop == '1':
        final_list = a.import_files()
        c_dict_all = a.cont_com(final_list)
        c_dict_most = a.main_com(final_list)
    elif loop == '2':
        if c_dict_all:
            a.print_commands(c_dict_all)
        else:
            print ("\nPlease, choose the option 1 first.\n")
    elif loop == '3':
        if c_dict_most:
            a.print_commands(c_dict_most)
        else:
            print ("\nPlease, choose the option 1 first.\n")
    elif loop == '4':
        if c_dict_all:
            c_dict_search = a.search_com(c_dict_all)
            a.print_commands(c_dict_search)
        else:
             print ("\nPlease, choose the option 1 first.\n")
    elif loop == '5':
        for x in open('./menus/menu_save.txt'):
            x = x.rstrip()
            print (x)
        c_dict_chose = input ("\nSelect one option to go: ")
        if c_dict_chose == '1' and c_dict_all:
            a.output_files(c_dict_all)
        elif c_dict_chose == '2' and c_dict_most:
            a.output_files(c_dict_most)
        elif c_dict_chose == '3' and c_dict_search:
            a.output_files(c_dict_search)
        else:
            print ("\nError! Choose a option first.\n")