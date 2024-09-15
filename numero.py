import re


def telefone(numero):
    a = r'^\([1-9]{2}\)9([0-9]{8}|[0-9]{4}\-[0-9]{4})$'

    if re.match(a, numero):
        return 1
    return 0



b = "(91)98169-2953"

print(telefone(b))