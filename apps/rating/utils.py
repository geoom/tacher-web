# -*- coding: utf-8 -*
import string
from random import choice

from django.utils.deconstruct import deconstructible


def generate_token(length=50):
    return ''.join([choice(string.letters + string.digits) for i in range(length)])


def generate_hash(length=10):
    return generate_token(length)


@deconstructible
class UploadTo(object):
    path = "uploads/{0}/{1}/{2}"

    def __init__(self, sub_path):
        self.sub_path = sub_path

    def __call__(self, instance, filename):
        return self.path.format(self.sub_path, generate_hash(7), filename)
