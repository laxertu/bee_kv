import argparse
import traceback

from bee_kv.public.driver.facade import Facade

parser = argparse.ArgumentParser(
                    prog='A simple KW data manager console',
                    description='Adds, edits removes and empties a KW repository of python objects',
                    epilog='Luca :-)')

subparsers = parser.add_subparsers(help='Kw management', dest="command")

parser_save = subparsers.add_parser('save', help='Saves a value')
parser_save.add_argument('key', type=str, help='Key')
parser_save.add_argument('value', help='Value')

parser_get = subparsers.add_parser('get', help='Gets a value by key')
parser_get.add_argument('key', help='Key of item')

parser_remove = subparsers.add_parser('remove', help='Removes a value by key')
parser_remove.add_argument('key', help='Key of item')

parser_remove = subparsers.add_parser('get_all', help='Gets all items')


parser_reset = subparsers.add_parser('reset', help='Reset repository')

args = parser.parse_args().__dict__

cmd = args['command']

try:
    if cmd == "save":
        Facade().save(args['key'], args['value'])
        print("Saved")
    elif cmd == "get":
        result = Facade().get(args['key']).payload
        print(result.key, result.value)
    elif cmd == "remove":
        Facade().remove(args['key'])
        print("Removed")
    elif cmd == "reset":
        Facade().reset()
        print("Resetted")
    elif cmd == "get_all":
        for k, item in Facade().get_all().items():
            print(item.key, item.value)


except Exception as e:
    print(f"[ERROR] {e}")

