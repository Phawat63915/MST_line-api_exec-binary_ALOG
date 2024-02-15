import argparse
import sys

class AtLeastOneRequired(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print("-----------------------------------")
        print("parser: ", parser)
        print("namespace: ", namespace)
        print("values: ", values)
        print("option_string: ", option_string)
        print("self.dest: ", self.dest)
        print("-----------------------------------")

        if getattr(namespace, self.dest) is None:
            setattr(namespace, self.dest, values)
        else:
            parser.error('At least -m or -b must be specified.')

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--message", action=AtLeastOneRequired, required=True, help="Message to send (max 1000 characters)")
parser.add_argument("-b", "--box_message", action=AtLeastOneRequired, required=True, help="Message to send from msg.toml config")

args = parser.parse_args()

# if args.message and args.box_message:
#     print("Both -m and -b cannot be specified. Only one or the other must be specified.")
#     sys.exit(1)

# print(args.message)
# print(args.box_message)
