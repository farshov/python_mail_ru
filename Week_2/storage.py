import argparse
import os
import tempfile
import json


def parser_storage():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", action="store_true",
                        help="Key")
    parser.add_argument("x", type=str,
                        help="value of key")
    parser.add_argument("--val", action="store",
                        help="Value", default=None, type=str)
    args = parser.parse_args()

    if args.val is not None:
        add_val(args.x, args.val)
    elif args.key:
        get_val(args.x)
    else:
        print('Smth wrong')


def add_val(key, val):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if os.path.isfile(storage_path):
        with open(storage_path, 'r') as f:
            storage = json.load(f)

        if key in storage.keys():
            storage[key].append(val)
        else:
            storage[key] = [val]
    else:
        storage = dict()
        storage[key] = [val]

    print(*storage[key], sep=', ')

    with open(storage_path, 'w') as f:
        json.dump(storage, f)


def get_val(key):
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    if os.path.isfile(storage_path):
        with open(storage_path, 'r') as f:
            storage = json.load(f)

        if key in storage.keys():
            print(*storage[key], sep=', ')
        else:
            print(None)
    else:
        print(None)


if __name__ == '__main__':
    parser_storage()