from data_base.operation_Crud import Operations_Crud
import keyboard

opc = Operations_Crud()


def insert_menu():
    print('Insert menu\n')
    name = input('Enter name ')
    street = input('Enter street ')
    city = input('Enter city ')
    phone = input('Enter Phone number ')
    opc.insert_db(name, street, city, phone)


def search_menu():
    column = search = op = None
    option = input('Would you like to take the full survey [Y] or [N] ')

    if option == 'Y' or option == 'y':
        op = '-1'
        column = 'FROM'
        search = 'tb_contacts'

    elif option == 'N' or option == 'n':
        op = '1'
        op_column = input('Wold you like to search by\n1 - Name\n2 - City\n3 - Cod\n')

        while True:
            if op_column == '1':
                column = 'T_NAME'
                break
            elif op_column == '2':
                column = 'T_CITY'
                break
            elif op_column == '3':
                column = 'N_ID'
                break
            else:
                print('Invalid Option')

        search = input('Enter yor search ')

    opc.search_db(op, column, search)


def update_menu():
    print('Welcome to the update menu type in what you want to update, if you dont want to update the data press enter')
    id = input('Type the [ID] you want to update ')
    validation = opc.search_db(-1, "N_ID", id)

    while True:
        if validation != -1:
            name = input('Name ')
            street = input('Street ')
            city = input('City ')
            opc.update(name, street, city, id)
            break
        else:
            id = input('Type the [ID] you want to update ')
        validation = opc.search_db(-1, "N_ID", id)


def delete_menu():
    print('point 0')

    while True:
        id = input('Welcome to the delete menu Type the [ID] you want to delete: ')
        validation = opc.search_db(-1, "N_ID", id)

        if validation != -1:
            option = input(f'Are you sure you want to delete id {id} [Y] or [N]')

            if option == 'Y' or option == 'y':
                opc.delete_db(id)
                print('pont 1')
                break
            else:
                break


def menu():
    start = True

    while start:

        option = input('Welcome to Menu - Enter a number\n1 - Insert\n2 - Search\n3 - Update\n4 - Delete\n5 - Exit\n')
        op_menu = 'y'

        if option in ['1', '2', '3', '4', '5']:

            while op_menu.lower() != 'n':

                if option == '1':
                    insert_menu()
                    op_menu = input('Do you want make a new insertion [Y] or [N]\n')

                if option == '2':
                    search_menu()
                    op_menu = input('Do you want make a new search [Y] or [N]\n')

                if option == '3':
                    update_menu()
                    op_menu = input('Do you want make a new update [Y] or [N]\n')

                if option == '4':
                    delete_menu()
                    op_menu = input('Do you want make a new update [Y] or [N]\n')

                if option == '5':
                    start = False
                    break
        else:
            print('Invalid Option')
            print("Press enter to continue...")
            keyboard.wait("enter")
            op_menu = input('')


menu()
