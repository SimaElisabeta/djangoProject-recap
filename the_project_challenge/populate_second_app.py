import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_project_challenge.settings')

import django
django.setup()

# FAKE POPULATION SCRIPT
from second_app.models import User
from faker import Faker

fakegen = Faker()


def populate(N=5):
    for entry in range(N):
        # create fake data for entry
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # create new user entry
        user_entry = User.objects.get_or_create(first_name=fake_first_name,
                                                last_name=fake_last_name,
                                                email=fake_email)[0]


if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('populating complete')
