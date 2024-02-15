# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('-t', action='store_true')

# args = parser.parse_args()

# if args.t:
#     # do something if -t is present
#     print("Argument -t is present")
# else:
#     # do something else if -t is not present
#     print("Argument -t is not present")

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--access_token", default=None)
# parser.add_argument("-t", "--access_token", nargs='?', default=None)
# nargs='?', default=None คือ ถ้าไม่ใส่ค่า จะเป็น None

args = parser.parse_args()

if args.access_token is not None:
    # do something if -t is present
    print("Argument -t is present with value:", args.access_token)
else:
    # do something else if -t is not present
    print("Argument -t is not present")
