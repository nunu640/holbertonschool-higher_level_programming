#!/usr/bin/python3
import marshal
def print_names():
    # hidden_4.pyc faylını oxumaq
    with open('/tmp/hidden_4.pyc', 'rb') as file:
        file.seek(16)  # `.pyc` faylında ilk 16 bayt magic header və timestamp-ə aiddir
        code = marshal.load(file)  # kodu marshal vasitəsilə yüklə
    # Moduldakı adları tapmaq
    names = dir(code)  # Modulun bütün atributlarının adlarını əldə et
    # Sadece '__' ilə başlamayan adları çap et
    for name in names:
        if not name.startswith('__'):
            print(name)
if __name__ == "__main__":
    print_names()
