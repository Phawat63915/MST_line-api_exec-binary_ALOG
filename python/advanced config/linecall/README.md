# Introduction
โปรแกรมนี้เป็นโปรแกรมสำหรับคุยกับ Line API ด้วย CLI Command Line Interface

# About
เนื่องด้วย Alog สำหรับการตั้ง Alert เมื่อเกิดเหตุการผิดปกติบางอย่างขึ้น จะมีช่องทางแจ้งเตือนเช่น Email, Slack หรือ สั่งเปิดโปรแกรมอื่นๆ ได้ แต่ไม่สามารถส่งแจ้งเตือนไปยัง Line ได้โดยตรง ตามที่ลูกค้าบางรายต้องการเพราะขี้เกียจเปิด Email ดูเป็นต้น ดังนั้น เพื่อให้ Alog สามารถแจ้งเตือนได้โดยตรง จึงมีการสร้างโปรแกรมนี้ขึ้นมาใช้ร่วมกับการสั่งเปิดโปรแกรม ซึ่ง กาารสั่งเปิดโปรแกรมนี้จะมี Input Fill ดังนี้

  1. path ที่อยู่ของโปรแกรม **Example:** ` C:\Windows\System32\WindowsPowerShell\v1. 0\powershell.exe`
  2. และ Argument ที่ต้องการส่งไปยังโปรแกรม **Example:** ` C:\Users\user\Documents\line.ps1 -message "Hello World" -token "<token>"`

โดยแกรมที่จะไม่ใช้ เป็น script powershell แต่เป็น .exe หรือ excutable เพื่อสามารถใช้ หลาย env หรือ Environment ได้ โดยที่ไม่ต้องติดตั้งโปรแกรมอื่นๆ

# OS Support
Windows
  * Windows 7-32bit (Not Support)
  * Windows 7-64bit (Not Support)
  * Windows 8-32bit (Not Support)
  * Windows 8-64bit (Not Support)
  * Windows 10-32bit (Support)
  * Windows 10-64bit (Support)
  * Windows 11-32bit (Support)
  * Windows 11-64bit (Support)
  * Windows Server 2008 (Not Support)
  * Windows Server 2012 (Not Support)
  * Windows Server 2016 (Support)
  * Windows Server 2019 (Support)
  * Windows Server 2022 (Support)

Linux
  * Ubuntu 16.04 (Not Support)
  * Ubuntu 18.04 (Not Support)
  * Ubuntu 20.04 (Not Support)
  * Ubuntu 21.04 (Not Support)
  * Debian 9 (Not Support)
  * Debian 10 (Not Support)
  * Debian 11 (Not Support)
  * CentOS 7 (Not Support)
  * CentOS 8 (Not Support)
  * Fedora 33 (Not Support)
  * Fedora 34 (Not Support)
  * Fedora 35 (Not Support)
  * Arch Linux (Not Support)
  * Manjaro (Not Support)
  * OpenSUSE (Not Support)
  * Alpine (Not Support)

โดยการรองจะถูกอัพเดทเพิ่มหากมีเวลาเพิ่มขึ้น (!)

# Feature
ซึ่งใช้การส่งข้อความผ่าน Line Notify ซึ่งจะส่งข้อความไปยัง Line ที่เราต้องการ โดยการส่งข้อความจะมี 2 แบบ คือ

### 1. ส่งข้อความแบบเดี่ยว

> โดยในรูปแบบนี้ จะใช้ Argument ในการส่งข้อความ โดยใช้ Argument เช่น `-m "hello"`

Example simple:
- **Path:** ` C:\line\linecall.exe`
- **Argument:** `-m "hello world"`

โดยสำหรับตัวเลือก Argument จะมีดังนี้
- `-m` หรือ `--message` สำหรับส่งข้อความ
- `-it` หรือ `--image_thumbnail` สำหรับส่ง URL ของรูปภาพ Thumbnail
- `-is` หรือ `--image_fullsize` สำหรับส่ง URL ของรูปภาพ Fullsize
- `-if` หรือ `--image_file` สำหรับส่ง Path ของรูปภาพ
- `-sp` หรือ `--sticker_package_id` สำหรับส่ง Package ID ของ Sticker
- `-si` หรือ `--sticker_id` สำหรับส่ง Sticker ID ของ Sticker
- `-nd` หรือ `--notification_disabled` สำหรับส่งข้อความโดยไม่แจ้งเตือน

### 2. ส่งข้อความแบบกลุ่ม จาก config

> โดยในรูปแบบนี้ จะไม่ใช้ Argument แต่จะใช้ config แทน ที่ถูกตั้งไว้ใน `msg.toml` ซึ่งจะอยู่ในโฟลเดอร์เดียวกับโปรแกรม

Example simple:
- **Path:** ` C:\line\linecall.exe`
- **Argument:** `-b msg1`

## คำสั่งแทนค่า config

> โดยหากใช้ `-t` หรือ `--access_token` จะให้ตัวโปรแกรมไม่ดึง token จาก config แต่จะใช้ token รับมาจาก Argument นี้แทน


- `-t` หรือ `--access_token` สำหรับส่ง Token ของ Line Notify

Example simple:
- **Path:** ` C:\line\linecall.exe`
- **Argument:** `-m "hello world" -t "J37Gduo8Dg"`

# Config
ซึ่งจะมี config.ini จะเป็น config ถูกใช้ทั้งใน 2 รูปแบบ
และ msg.toml จะเป็น config ที่ใช้ในรูปแบบที่ 2 ซึ่งสามารถเพิ่มชุดข้อความได้โดยการ เพิ่มหัวข้อใหม่

# CLI Command
- `-h` หรือ `--help` สำหรับดูคำสั่งทั้งหมด
```txt
usage: linecall.exe [-h] [-m MESSAGE] [-b BOX_MESSAGE] [-t ACCESS_TOKEN] [-it IMAGE_THUMBNAIL] [-is IMAGE_FULLSIZE]
                    [-if IMAGE_FILE] [-sp STICKER_PACKAGE_ID] [-si STICKER_ID] [-nd NOTIFICATION_DISABLED]

Send a message via LINE Notify

options:
  -h, --help            show this help message and exit
  -m MESSAGE, --message MESSAGE
                        Message to send (max 1000 characters)
  -b BOX_MESSAGE, --box_message BOX_MESSAGE
                        Message to send from msg.toml config
  -t ACCESS_TOKEN, --access_token ACCESS_TOKEN
                        LINE Notify access token
  -it IMAGE_THUMBNAIL, --image_thumbnail IMAGE_THUMBNAIL
                        HTTP/HTTPS URL of the image thumbnail (max 240x240px JPEG)
  -is IMAGE_FULLSIZE, --image_fullsize IMAGE_FULLSIZE
                        HTTP/HTTPS URL of the full-size image (max 2048x2048px JPEG)
  -if IMAGE_FILE, --image_file IMAGE_FILE
                        Path to the image file (PNG or JPEG)
  -sp STICKER_PACKAGE_ID, --sticker_package_id STICKER_PACKAGE_ID
                        Sticker package ID
  -si STICKER_ID, --sticker_id STICKER_ID
                        Sticker ID
  -nd NOTIFICATION_DISABLED, --notification_disabled NOTIFICATION_DISABLED
                        Disable push notification

Created by © 2023 Magic Software Thailand Corp.,Ltd. (Phawat)
```