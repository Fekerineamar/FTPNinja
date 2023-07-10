import argparse
import socket
import signal
import time
import sys
import os
import re
import ftplib

def logo():
    os.system("clear")
    print("\033[38;5;111m")
    print("""
           _____________  _  ___        _     
          / __/_  __/ _ \/ |/ (_)__    (_)__ _
         / _/  / / / ___/    / / _ \  / / _ `/
        /_/   /_/ /_/  /_/|_/_/_//_/_/ /\_,_/ 
                                  |___/       
                          By Cody4code v1.0.1
    """)
    print("\033[0m")



def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False


def get_status_from_exception(exception):
    pattern = r"\b(\d{3})\b"
    match = re.search(pattern, str(exception))
    if match:
        return match.group()
    else:
        return ""


def is_valid_ftp_ip(ip, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        with ftplib.FTP(ip) as ftp:
            return True
    except ftplib.error_perm as e:
        if "No connections allowed from your IP" in str(e):
            return "NOT_ALLOWED"
        else:
            raise
    except (socket.timeout, socket.error):
        return False


def connect_ftp(ip, output_file):
    try:
        if not is_valid_ip(ip):
            print(f" Invalid IP: \033[38;5;196m{ip}\033[0m Address")
            return
        elif not is_valid_ftp_ip(ip):
            print(f" Invalid FTP IP: \033[38;5;196m{ip}\033[0m Address")
            return
        elif is_valid_ftp_ip(ip) == "NOT_ALLOWED":
            print(f" Error connecting to {ip}: [\033[38;5;203m550\033[0m] No connections allowed from your IP")
            return

        with ftplib.FTP(ip) as ftp:
            ftp.login()
        print(f" Successfully logged in to IP: {ip} \033[38;5;82m[200]\033[0m \033[38;5;111mLogin Success\033[0m")
        if output_file is not None:
            output_file.write(f" Successfully logged in to IP: {ip}\n")
    except ftplib.error_perm as e:
        status = get_status_from_exception(e)
        if status:
            print(f" Error connecting to {ip}: [\033[38;5;203m{status}\033[0m] \033[91m{str(e)[len(status)+1:]}\033[0m")
    except (socket.timeout, socket.error):
        print(f" Error connecting to {ip}: \033[38;5;203mConnection timed out or socket error\033[0m")
    except Exception as e:
        status = get_status_from_exception(e)
        if status:
            print(f" Error connecting to {ip}: [\033[38;5;203m{status}\033[0m] \033[91m{str(e)[len(status)+1:]}\033[0m")
        if output_file is not None:
            output_file.write(f" An unexpected error occurred while connecting to {ip}: {str(e)}\n")


def process_ips(ip_list, output_file):
    for ip in ip_list:
        connect_ftp(ip, output_file)

parser = argparse.ArgumentParser(description='FTP Tool')
parser.add_argument('-l', '--list', metavar='ipList.txt', help='File containing a list of IP addresses')
parser.add_argument('-d', '--single-ip', metavar='IP', help='Single IP address')
parser.add_argument('-o', '--output', metavar='output.txt', type=str, help='Output file')


def parse_arguments():
    args = parser.parse_args()
    ip_list = []
    if args.list:
        with open(args.list, 'r') as ip_file:
            ip_list = [line.strip() for line in ip_file if is_valid_ip(line.strip())]
    elif not sys.stdin.isatty():
        ip_list = [line.strip() for line in sys.stdin if is_valid_ip(line.strip())]
    if args.single_ip:
        ip_list.append(args.single_ip)
    return args, ip_list

def main():
    args, ip_list = parse_arguments()
    if args.list:
        print(f" \033[0;33mIP_List: {args.list}\033[0m")
        with open(args.list, 'r') as ip_file:
            lines = sum(1 for _ in ip_file)
        print(f" \033[0;36mSize: {lines} IP lines\033[0m")
    elif not sys.stdin.isatty():
        print(f" \033[0;33mIP_List: {args.list}\033[0m")
        lines = sum(1 for _ in sys.stdin)
        print(f" \033[0;36mSize: {lines} IP lines\033[0m")
    output_file = None
    if args.output:
        output_file = open(args.output, 'w')
    if not sys.stdin.isatty() or args.list or args.single_ip:
        print(f" \033[0;32m[{time.strftime('%Y-%m-%d %H:%M:%S')}] Starting...\033[0m")

        try:
            process_ips(ip_list, output_file)
        except KeyboardInterrupt:
            print("\n\033[48;2;255;0;0m\033[38;2;255;255;255mCanceled by user.\033[0m")
    else:
        parser.print_help()
    if output_file:
        output_file.close()

if __name__ == '__main__':
    logo()
    main()


