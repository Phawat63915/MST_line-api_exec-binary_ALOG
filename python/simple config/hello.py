import os
import argparse
import configparser
import requests

def send_line_notify(args):
    url = "https://notify-api.line.me/api/notify"
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
    print(response.status_code)
    print(response.text)

def read_config():
    config_path = "config.ini"
    
    if not os.path.isfile(config_path):
        print("Error: Config file not found. Please create a 'config.ini' file.\n")
        exit(1)
    
    config = configparser.ConfigParser()
    config.read(config_path)
    return config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Send a message via LINE Notify",
        epilog="Created by © 2023 Magic Software Thailand Corp.,Ltd. (Phawat)",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-m", "--message", required=True, help="Message to send (max 1000 characters)")
    parser.add_argument("-t", "--access_token", help="LINE Notify access token")
    parser.add_argument("-it", "--image_thumbnail", help="HTTP/HTTPS URL of the image thumbnail (max 240x240px JPEG)")
    parser.add_argument("-is", "--image_fullsize", help="HTTP/HTTPS URL of the full-size image (max 2048x2048px JPEG)")
    parser.add_argument("-if", "--image_file", help="Path to the image file (PNG or JPEG)")
    parser.add_argument("-sp", "--sticker_package_id", type=int, help="Sticker package ID")
    parser.add_argument("-si", "--sticker_id", type=int, help="Sticker ID")
    parser.add_argument("-nd", "--notification_disabled", action='store_true', help="Disable push notification")

    args = parser.parse_args()

    if args.access_token:
        access_token = args.access_token
    else:
        config = read_config()
        access_token = config.get("LINE", "access_token")
        args.access_token = access_token

    send_line_notify(args)
