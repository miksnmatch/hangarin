import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

import random
from faker import Faker
from django.utils import timezone
from taskmanager.models import Task, SubTask, Note, Category, Priority

fake = Faker()

categories = list(Category.objects.all())
priorities = list(Priority.objects.all())

for _ in range(20):
    task = Task.objects.create(
        title=fake.sentence(nb_words=5),
        description=fake.paragraph(nb_sentences=3),
        status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
        deadline=timezone.make_aware(fake.date_time_this_month()),
        category=random.choice(categories),
        priority=random.choice(priorities),
    )

    for _ in range(3):
        SubTask.objects.create(
            task=task,
            title=fake.sentence(nb_words=4),
            status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
        )

    for _ in range(2):
        Note.objects.create(
            task=task,
            content=fake.paragraph(nb_sentences=2),
        )

print("DONE POPULATING DATA")