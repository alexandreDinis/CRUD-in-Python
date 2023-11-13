import sqlite3

from .connect_DB import Connect_DB


class Operations_Crud:
    def __init__(self):
        path = r'C:\WorkSpace\Dinis\Estudo\1 - Semestre\Programação\python3\Banco\Client.db'
        self.receiver = Connect_DB(path)

    def insert_db(self, T_NAME, T_STREET, T_CITY,T_PHONE_NUMBER):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO tb_contacts VALUES(NULL, ?, ?, ?, ?)', (T_NAME, T_STREET, T_CITY,
                                                                                 T_PHONE_NUMBER))
            connection.commit()
            print('\nInsert successfully\n')
        except sqlite3.Error as e:
            print('Insert not successfully', e)
        finally:
            self.receiver.close_connection()

    def search_db(self,opc,column, search):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            if opc != '-1':
                cursor.execute(f'SELECT * FROM tb_contacts WHERE {column} = ?',(search,))
                result = cursor.fetchall()
                if result:
                    print("\nContacts found:")
                    print("{:<5} {:<20} {:<30} {:<15} {:<15}".format("ID", "Name", "Street", "City", "Phone"))
                    print("-" * 80)
                    for results in result:
                        print("{:<5} {:<20} {:<30} {:<15} {:<15}".format(results[0], results[1], results[2], results[3],
                                                                         results[4]))
                    print("-" * 80)

                else:
                    print('Contact not found')
                    return -1
            if opc == '-1':
                cursor.execute(f'SELECT * {column} {search}')
                result = cursor.fetchall()
                if result:
                    print("\nContacts found:")
                    print("{:<5} {:<20} {:<30} {:<15} {:<15}".format("ID", "Name", "Street", "City", "Phone"))
                    print("-" * 80)
                    for results in result:
                        print("{:<5} {:<20} {:<30} {:<15} {:<15}".format(results[0], results[1], results[2], results[3],
                                                                         results[4]))
                    print("-" * 80)
                else:
                    print('Contact not found')
        except sqlite3.Error as e:
            print('Error in search', e)
        finally:
            self.receiver.close_connection()

    def update(self,T_NAME, T_STREET, T_CITY,N_ID):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            set_values = ""
            values = []

            validation = self.search_db(-1,'N_ID',N_ID)

            if validation != -1:

                if T_NAME is not None and T_NAME.strip() != "":
                    set_values += "T_NAME=?, "
                    values.append(T_NAME)
                else:
                    cursor.execute(f'SELECT T_NAME FROM tb_contacts WHERE N_ID = ?', (N_ID,))
                    set_values += "T_NAME=?, "
                    T_NAME = cursor.fetchone()[0]
                    values.append(T_NAME)

                if T_STREET is not None and T_STREET.strip() != "":
                    set_values += "T_STREET = ?, "
                    values.append(T_STREET)
                else:
                    cursor.execute(f'SELECT T_STREET FROM tb_contacts WHERE N_ID = ?', (N_ID,))
                    set_values += "T_STREET = ?, "
                    T_STREET = cursor.fetchone()[0]
                    values.append(T_STREET)

                if T_CITY is not None and T_CITY.strip() != "":
                    set_values += "T_CITY = ?, "
                    values.append(T_CITY)
                else:
                    cursor.execute(f'SELECT T_CITY FROM tb_contacts WHERE N_ID = ?', (N_ID,))
                    set_values += "T_CITY = ?, "
                    T_CITY = cursor.fetchone()[0]
                    values.append(T_CITY)

                if set_values:
                    set_values = set_values.rstrip(', ')

                query = f'UPDATE tb_contacts SET {set_values} WHERE N_ID = ?'
                values.append(N_ID)
                cursor.execute(query,tuple(values))

                connection.commit()

                print('Database update successfully\n')
                print()
                self.search_db(-1,'N_ID',N_ID)

        except sqlite3.Error as e:
            print('Error when update',e)
        finally:
            self.receiver.close_connection()

    def delete_db(self,T_ID):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM tb_contacts WHERE N_ID = ?", (T_ID,))
            connection.commit()
            print('Delete data successfully')
        except sqlite3.Error as e:
            print(f'Error Delete ', {e})
        finally:
            self.receiver.close_connection()

