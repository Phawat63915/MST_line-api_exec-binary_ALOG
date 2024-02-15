import os
import argparse
import configparser #for ini
import requests
import toml
import sys

def send_line_notify(args, url):
    access_token = args.access_token
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    data = {
        "message": args.message,
        "stickerPackageId": args.sticker_package_id,
        "stickerId": args.sticker_id,
        "notificationDisabled": args.notification_disabled
    }

    files = {}
    if args.image_file:
        files["imageFile"] = open(args.image_file, "rb")

    response = requests.post(url, headers=headers, data=data, files=files)
    print(response.text)

def read_config():
    config_path = "config.ini"
    
    if not os.path.isfile(config_path):
        print("Error: Config file not found. Please create a 'config.ini' file.\n")
        sys.exit(0)
    
    config = configparser.ConfigParser()
    config.read(config_path)
    return config

def read_msg_config(msg_name):
    msg_config_path = "msg.toml"

    if not os.path.isfile(msg_config_path):
        print("Error: Message config file not found. Please create a 'msg.toml' file.")
        sys.exit(0)

    msg_config = toml.load(msg_config_path)

    if msg_name not in msg_config:
        print(f"Error: Message section '{msg_name}' not found in 'msg.toml'.")
        sys.exit(0)

    return msg_config[msg_name]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Send a message via LINE Notify",
        epilog="Created by © 2023 Magic Software Thailand Corp.,Ltd. (Phawat)",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-m", "--message", required=False, help="Message to send (max 1000 characters)")
    parser.add_argument("-b", "--box_message", required=False, help="Message to send from msg.toml config")
    parser.add_argument("-t", "--access_token", help="LINE Notify access token")
    parser.add_argument("-it", "--image_thumbnail", help="HTTP/HTTPS URL of the image thumbnail (max 240x240px JPEG)")
    parser.add_argument("-is", "--image_fullsize", help="HTTP/HTTPS URL of the full-size image (max 2048x2048px JPEG)")
    parser.add_argument("-if", "--image_file", help="Path to the image file (PNG or JPEG)")
    parser.add_argument("-sp", "--sticker_package_id", type=int, help="Sticker package ID")
    parser.add_argument("-si", "--sticker_id", type=int, help="Sticker ID")
    parser.add_argument("-nd", "--notification_disabled", help="Disable push notification")

    args = parser.parse_args()

    if args.access_token:
        access_token = args.access_token
    else:
        config = read_config()
        access_token = config.get("LINE", "access_token")
        url = config.get("LINE", "url")
        args.access_token = access_token

    if args.message is None and args.box_message is None:
        print("Error: You must specify a message to send. please use -m or -b.")
        print("using -h show this help message.")
        sys.exit(0)

    if args.box_message is not None:
        # if hell แก้ไขปัญชั่วคราว หากมีเวลามากกว่านี้จะแก้ไข ในวิธีที่โอเครกว่า
        if args.message is not None:
            print("Error: You can't use -m and -b at the same time.")
            sys.exit(0)
        if args.image_thumbnail is not None:
            print("Error: You can't use -it and -b at the same time.")
            sys.exit(0)
        if args.image_fullsize is not None:
            print("Error: You can't use -is and -b at the same time.")
            sys.exit(0)
        if args.image_file is not None:
            print("Error: You can't use -if and -b at the same time.")
            sys.exit(0)
        if args.sticker_package_id is not None:
            print("Error: You can't use -sp and -b at the same time.")
            sys.exit(0)
        if args.sticker_id is not None:
            print("Error: You can't use -si and -b at the same time.")
            sys.exit(0)
        if args.notification_disabled is not None:
            print("Error: You can't use -nd and -b at the same time.")
            sys.exit(0)
        msg_section = read_msg_config(args.box_message)
        args.message = msg_section.get("message", None)
        args.image_thumbnail = msg_section.get("image_thumbnail", None)
        args.image_fullsize = msg_section.get("image_fullsize", None)
        args.image_file = msg_section.get("image_filename", None)
        args.sticker_package_id = int(msg_section.get("sticker_package_id", None))
        args.sticker_id = int(msg_section.get("sticker_id", None))
        args.notification_disabled = msg_section.get("notification_disabled", None)

    send_line_notify(args, url)

