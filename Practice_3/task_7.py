# -*- coding: utf-8 -*-
"""


"""
# email хранит адрес
# не удаляйте функцию validate, напишите свою реализацию
import re

WEBSITE_CHARS = "zxcvbnmasdfghjklqwertyuiop0123456789"
USERNAME_CHARS = WEBSITE_CHARS + "_-"


def validate_regexp(email):
    return bool(re.fullmatch(r'^[a-z0-9_-]+@[a-z0-9]+\.[a-z0-9]{1,3}$',
                             email.lower(),
                             flags=re.ASCII))


def validate_classic(email):
    email = email.lower()

    if email.count("@") != 1 or email.count(".") != 1:
        return False
    if email.find("@") > email.find("."):
        return False

    username, _, site_plus_ext = email.partition("@")
    websitename, _, extension = site_plus_ext.partition(".")

    if len(extension) > 3:
        return False

    if len([x for x in websitename if x not in WEBSITE_CHARS]):
        return False

    if len([x for x in username if x not in USERNAME_CHARS]):
        return False

    return True


def validate(email):
    return validate_regexp(email)
