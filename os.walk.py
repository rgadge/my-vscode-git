import os
path = "/Users/rajneeshgadge/Applications"

passwd = "/etc/passwd"


def get_uid(passwd):
    for line in open(passwd):
        if not line.startswith("#"):
            uid = line.split(":")
            print(uid[2])
        else:
            continue

get_uid(passwd)

