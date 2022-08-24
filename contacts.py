from peewee import *

db = PostgresqlDatabase('contacts', user='cjames222', password='',
                        host='localhost', port=5433)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone_number = BigIntegerField()

# db.drop_tables([Contact])
db.create_tables([Contact])



def create_contact():
    first_name = input('Create A Contact \nFirst Name: ')
    last_name = input('Last Name: ')
    phone_number = input('Phone Number: ')

    new_contact = Contact(first_name=first_name, last_name=last_name, phone_number=phone_number)

    new_contact.save()
    print('Contact Saved!')

def update_contact():
    contacts = Contact.select().count()

    if contacts == 0:
        print('No Contacts Saved In Contact Book!')
        contact_book()
    
    user = input('Type first name: ')
    for contact in Contact.select():
        if user == contact.first_name:
            found = Contact.get(Contact.first_name == user)
            print(found)
        elif user != contact.first_name:
            print('Contact Not Found!')
            contact_book()

    new_first_name = input('New First Name: ')
    new_last_name = input('New Last Name: ')
    new_phone_number = input('New Phone Number: ')

    update = Contact.update({Contact.first_name:new_first_name, Contact.last_name:new_last_name, Contact.phone_number:new_phone_number}).where(Contact.first_name==found.first_name, Contact.last_name==found.last_name, Contact.phone_number==found.phone_number)

    update.execute()
    print('Contact Updated!')

def find_contact():
    contacts = Contact.select().count()

    if contacts == 0:
        print('No Contacts Saved In Contact Book!')
        contact_book()
    
    user = input('Type first name: ')
    for contact in Contact.select():
        if user == contact.first_name:
            found = Contact.select().where (Contact.first_name==user)
            print(found)
        elif user != contact.first_name:
            print('Contact Not Found!')

def see_contacts():
    for contact in Contact.select():
            all_contacts = contact.first_name, contact.last_name, contact.phone_number
            print(all_contacts)

def delete_contact():
    first_name = input('Type first name: ')
    last_name = input('Type last name: ')
    for contact in Contact.select():
        if first_name == contact.first_name and last_name == contact.last_name:
            delete = Contact.delete().where (Contact.id==contact)
            delete.execute()
            print('Contact Deleted!')  

def delete_all_contacts():
    user = input('Are you sure?: ')

    if user != 'y' and user != 'n':
        print('Invalid Input!')
        delete_all_contacts()

    if user == 'y':
        delete = Contact.delete()
        delete.execute()
        print('All contacts deleted!')
        contact_book()
    elif user == 'n':
        print('Operation cancelled')
        contact_book()


input('Welcome to Contact Book!')

def contact_book():
    
    user = input('What would you like to do? ')
    if user != 'New Contact' and user != 'See Contacts' and user != 'Update Contact' and user != 'Find Contact' and user != 'Delete Contact' and user != 'Delete All' and user != 'exit':
        print('Invalid Input!')
        contact_book()
    elif user == 'New Contact':
        create_contact()
        contact_book()
    elif user == 'See Contacts':
        see_contacts()
        contact_book()
    elif user == 'Update Contact':
        update_contact()
        contact_book()
    elif user == 'Find Contact':
        find_contact()
        contact_book()
    elif user == 'Delete Contact':
        delete_contact()
        contact_book()
    elif user == 'Delete All':
        delete_all_contacts()
    elif user == 'exit':
        print('Exiting...')
        quit()


contact_book()