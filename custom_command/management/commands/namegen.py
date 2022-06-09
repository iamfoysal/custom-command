from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import names




#random string using name gen
class Command (BaseCommand):
    help = 'Random name generator !!'
    def handle(self, *args, **kwrgs):
        name = get_random_string(length=15)
        self.stdout.write(name)

        self.stdout.write('----------New name---------- \nName: %s \nname Generate Succesfully Completed! \n\n'% (name))

#real name gen
        print("\nMail Name \n ")

        for i in range(15):
            rand_name=names.get_full_name(gender='male')
            print(rand_name)
        


        print("\n Femail Name \n")
        for i in range(15):
            rand_name = names.get_full_name(gender='female')
            print(rand_name)
        