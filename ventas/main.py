import sys
import csv
import os


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)

def _save_clients_to_storage():
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
        print('Client already is in the client\'s list')


def list_clients():
    print(''' 
uid  |  name  | company |   email   | position
************************************************************************
    
    ''')
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'
        .format(
            uid=idx, 
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']
        ))


def update_client(client_name):
    global clients
    client = search_client(client_name)
    if client:
        print('****Update to client*****')

        index = clients.index(client)
        clients[index] = _get_client_info()
    else:
        _no_clients_list()


def delete_client(client_name):
    global clients
    client = search_client(client_name)
    if client:
        clients.remove(client)
    else:
        _no_clients_list()


def search_client(client_name):
    
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return client
    
    return {}

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)#imprimir 50 beces el asterisco
    print('What would you like to do doday?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_field(field_name):
    field = None
    
    while not field:
        field = input('What is the client {}?'.format(field_name))

    return field
    

def _get_client_name():
    # client_name = None

    # while not client_name:
    #     client_name = input('What is the client name? ')

    #     if client_name == 'exit':
    #         client_name = None
    #         break
        
    # if not client_name:
    #     sys.exit()
        
    # return client_name

    return input('What is the client name? ')


def _get_client_info():
    return {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position')
    }


def _no_clients_list():
    return print('Client is not in client\'s list')

if __name__ == '__main__':
    _initialize_clients_from_storage()
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_client_info()

        create_client(client)
    elif command == 'L':
        list_clients()
    elif command == 'D':
        client_name = _get_client_field("name")               

        delete_client(client_name)

        pass
    elif command == 'U':
        client_name = _get_client_field("name")

        update_client(client_name)

        pass
    elif command == 'S':
        client_name = _get_client_field("name")
        client = search_client(client_name)

        if client:
            print('The client: {} is in the client\'s list'.format(client_name))
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))

        pass
    else:
        print('Invalid command')


    _save_clients_to_storage()
