import os
#Set the environment
os.environ.setdefault('DJANGO_SETTING_MODULE', 'first_project.settings')
# export DJANGO_SETTINGS_MODULE=first_project.settings (you need to run this command if you are using linux)
import django
django.setup()

## FAKE POP SCRIPT
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fakegen = Faker()
topics = ["Search", "Social", "Marketplace", "News", "Games"]


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t    

def polpulate(N=5):
    """
    Create fake data including the webpage entry and record 
    """
    for entry in range(N):
        #get the topic for the entry
        top = add_topic()
        #Create the fake date for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url = fake_url, name= fake_name)[0]

        # Create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("populating script")
    polpulate(20)
    print("populating complete")


