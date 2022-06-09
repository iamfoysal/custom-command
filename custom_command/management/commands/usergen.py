import email
from multiprocessing import context
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'DataBase random user generator'

    def add_arguments(self, parser):
        parser.add_argument('qty', type=int, help='The amount of users to create')
        parser.add_argument('-a', '--admin', action='store_true', help='Define an admin account')

    def handle(self, *args, **kwargs):
        qty = kwargs['qty']
        admin = kwargs['admin']

        for User_Range in range(qty):
            username = get_random_string(10)
            email = username +'@gmail.com'
            password = get_random_string(10)

            # context ={'username':username, 'email': '', 'password':password}
            if admin:
                User.objects.create_superuser(username=username, email= email, password=password)
            else:
                User.objects.create_user(username=username, email= email, password=password)

            self.stdout.write('===========New User========== \nusername: %s\nemail: %s\npassword : %s  \naccount created Succesfully Completed! \n\n'% (username, email, password))