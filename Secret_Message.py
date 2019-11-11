#  Copyright (c) 2019.
#  @Author : Lassina OUATTARA
#  @Python code
import os


def rename_files():
    # get the ist of file in the folder
    file_list = os.listdir("Message/")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir("Message/")
    # for each file rename it
    t_table = dict.fromkeys(map(ord, '0123456789'), None)
    print(t_table)
    for file_name in file_list:
        new_name = file_name.translate(t_table)
        os.rename(file_name, new_name)
        print(F"{file_name} renamed to {new_name}")

        os.chdir(saved_path)


rename_files()
