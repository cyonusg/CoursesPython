import click
from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """ Manages the clients lifecycle"""
    pass

@clients.command()
@click.option('-n','--name',
              type=str,
              prompt=True,
              help='The client name')
@click.option('-c','--company',
              type=str,
              prompt=True,
              help='The client compay')
@click.option('-e','--email',
              type=str,
              prompt=True,
              help='The client email')
@click.option('-p','--position',
              type=str,
              prompt=True,
              help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client"""
    client = Client(name, company, email,position)
    client_service = ClientService(ctx.obj['clients_table'])
    print(client)
    client_service.create_client(client)

@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    clients = client_service.list_clients()
    print(clients)
    click.echo(' ID | NAME | COMPANY | EMAIL | POSITION')
    click.echo('*' * 100)
    for client in clients:
        click.echo('{uid} | {name} | {company} | {email} | {position}'.format(uid=client['uid'],
                                                                         name=client['name'],
                                                                         company=client['company'],
                                                                         email=client['email'],
                                                                         position=client['position']))

@clients.command()
@click.argument('client_id', type=str)
@click.pass_context
def update(ctx, client_id):
    """Updated a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()
    client = [client for client in client_list if client['uid'] == client_id]
    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)

        click.echo('Client updated')
    else: 
        click.echo('client not found')
    pass

def _update_client_flow(client):
    click.echo('Leave empty if you don\'t want to modify a value')

    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)

    return client

@clients.command()
@click.argument('client_id', type=str)
@click.pass_context
def delete(ctx, client_id):
    """Deletes a client"""
    client_service = ClientService(ctx.obj['clients_table'])

    if click.confirm('Are you sure you want to delete the client with uid: {}'.format(client_id)):
        client_service.delete_client(client_id)


all = clients

all = clients
