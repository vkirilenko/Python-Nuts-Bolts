#!/usr/bin/env python3

import os, sys, datetime
from pathlib import Path
from collections import defaultdict
from hashlib import md5

try:
    directory = Path(sys.argv[1])
except:
    directory = Path.cwd()

def make_config():
    path = Path(directory, 'conf.txt')
    if not path.exists():
        path.parent.mkdir(exist_ok=True, parents=True)
        path.touch()
    print(path)
    return path

def add_data(conf):
    with open(conf, mode='wt') as config:
        config.write(datetime.date.today().strftime('%m/%d/%y') + '\nENV = some_value')
    config.close()

def print_conf(conf):
    if conf.is_file():
        print("\nPrinting config:\n")
        print(conf.read_text(), end = '\n')

def find_files(filepath):
    for path in Path(filepath).rglob('*'):
        if path.is_file():
            yield path

def check_files():
    file_hashes = defaultdict(list)
    for path in find_files(Path.cwd()):
        file_hash = md5(path.read_bytes()).hexdigest()
        file_hashes[file_hash].append(path)

    for paths in file_hashes.values():
        if len(paths) > 1:
            print("Duplicate files found:")
            print(*paths, sep='\n')

def choose():
    while True:
        opt = input("Choose mode:\n1 - config file\n2 - duplicate search\nEnter a number: ")
        if opt == "1":
            conf = make_config()
            add_data(conf)
            print_conf(conf)
            sys.exit(0)
        elif opt == "2":
            check_files()
            sys.exit(0)
        else:
            print("You have to choose only from two options!")
            continue

if __name__ == "__main__":
    choose()


