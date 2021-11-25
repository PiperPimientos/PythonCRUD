import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Sofware Engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data Engineer',
    },
]

def create_client(client):

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'
        .format(uid=idx, 
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']
        ))


def update_client(client_name):
    client = search_client(client_name)
    if client:
        print('****Update to client*****')

        index = clients.index(client)
        clients[index] = _get_client_info()
    else:
        _no_clients_list()


def delete_client(client_name):
    client = search_client(client_name)
    if client:
        clients.remove(client)
    else:
        _no_clients_list()


def search_client(client_name):
    
    for client in clients:
        if client['name'].capitalize() != client_name.capitalize():
            continue
        else:
            return client
    
    return {}

def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)#imprimir 50 beces el asterisco
    print('What would you like to do doday?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')


def _get_client_field(field_name):
    field = None
    
    while not field:
        field = input('What is the client {}?'.format(field_name))

    return field
    

def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')

        if client_name == 'exit':
            client_name = None
            break
        
    if not client_name:
        sys.exit()
        
    return client_name


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
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_client_info()

        create_client(client)
        list_clients()
    elif command == 'D':
        client_name = _get_client_field("name")               

        delete_client(client_name)
        list_clients()
        pass
    elif command == 'U':
        client_name = _get_client_field("name")

        update_client(client_name)
        list_clients()
        pass
    elif command == 'S':
        client_name = _get_client_field("name")
        client = search_client(client_name)

        if client:
            print('The client: {} is in the client\'s list'.format(client_name))
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))

        list_clients()
        pass
    else:
        print('Invalid command')
