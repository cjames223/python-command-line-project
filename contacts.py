from peewee import *

db = PostgresqlDatabase('contacts', user='cjames222', password='',
                        host='localhost', port=5433)

db.connect()

class BaseModel(Model):
    class Meta:
        database =db

class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone_number = IntegerField()

# db.drop_tables([Contact])
db.create_tables([Contact])



def create_contact():
    first_name = input('Create A Contact \n First Name: ')
    last_name = input('Last Name: ')
    phone_number = input('Phone Number: ')

    new_contact = Contact(first_name=first_name, last_name=last_name, phone_number=phone_number)
    new_contact.save()

def find_contact():
    user = input('Type first name: ')
    for contact in Contact.select():
        if user == contact.first_name:
            print(contact.first_name, contact.last_name, contact.phone_number)

input('Welcome to Contact Book!')

def contact_book():
    
    user = input('What would you like to do? ')
    if user == 'New Contact':
        create_contact()
        contact_book()
    elif user == 'See Contacts':
        for contact in Contact.select():
            print(contact.first_name, contact.last_name, contact.phone_number)
            contact_book()
    elif user == 'Find Contact':
        find_contact()
        contact_book()
    elif user == 'exit':
        print('Exiting...')


contact_book()