
import sys
import csv
import os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA= ['uid','name', 'company', 'email', 'position']
clients = []

def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    global clients
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)

    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table_name, CLIENT_TABLE)

def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the clients')

def list_clients():
    global clients
    print('uid |  name  | company  | email  | position ')
    print('*' * 50)
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {email} | {company} | {position}'.format(
            uid=idx,
            name= client.get('name'),
            email= client.get('email'),
            company= client.get('company'),
            position= client.get('position'),
        ))

def update_client(client_id, update_client_name):
    global clients
    if len(clients) - 1 >= client_id:
        clients[client_id]= update_client_name
    else:
        print('client not found')

def delete_client(index):
    global clients
    clients.pop(index)

def search_client(client_name):
    global clients
    for client in clients:
            if client != client_name:
                continue
            else:
                return True


#utils begin
def _get_client_field(message):
    client_name = None

    while not client_name:
        client_name = input(message)
        if client_name == 'exit':
            client_name = None
        break
    if not client_name:
        sys.exit()
    return client_name

def _check_option_user(option):
        match option:
            case 'C':
                client = _build_user_dictionary()
                create_client(client)
            case 'D':
                list_clients()
                index = _get_client_field('Insert the id of clients you want to delete: ')
                delete_client(int(index))
                print('DELETE')
            case  'U':
                id = _get_client_field('Insert the id of clients you want to update: ')
                updated_client_name = _build_user_dictionary()
                update_client(int(id), updated_client_name)
                print('UPDATE')
            case 'S':
                client_name = _get_client_field('What is the client name?: ')
                found = search_client(client_name)
                if(found) : 
                    print('Clients exist')
                else:
                    print(f'The client:{client_name} is not our clients')
            case 'L':
                list_clients()
            case _:
                print('Invalid command')

def _build_user_dictionary():
    return {
            'name': _get_client_field('What is the client name?: '),
            'company': _get_client_field('What is the company name?: '),
            'email': _get_client_field('What is the email?: '),
            'position': _get_client_field('What is the position?: '),
        }
#utils ends

def _print_welcome():
    _initialize_clients_from_storage()
    print('Welcome to platzi ventas')
    print('*'*50)
    print('What would you like to do today')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print('[L]ist clients')
if __name__ == '__main__':  
    _print_welcome()
    
    command = (input()).upper()

    _check_option_user(command)

    #list_clients()

    _save_clients_to_storage()