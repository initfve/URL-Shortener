import random
import string

from django.core.exceptions import ObjectDoesNotExist

from .models import Link


def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def getFreeLink(length):
    random_link = randomString(length)
    while Link.objects.filter(short_url=random_link).count():
        random_link = randomString(length)
    return random_link
