from paths import FILE_DATA


def load_file():
    with open(FILE_DATA) as f:
        dict_all = f.readlines()
    return dict_all
