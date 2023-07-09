import argparse
import socket
from ftplib import FTP
import sys
import os
import subprocess

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

logo()
def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def is_ip_reachable(ip, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((ip, 21))
        return True
    except (socket.timeout, socket.error):
        return False

def connect_ftp(ip, output_file):
    if not is_valid_ip(ip):
        print(f"Invalid IP: {ip}")
        return

    if not is_ip_reachable(ip):
        print(f"No response from IP: {ip}")
        return

    try:
        ftp = FTP()
        ftp.connect(ip)
        ftp.login()
        print(f"Successful login for IP: {ip}")
        if output_file is not None:
            output_file.write(f"Successful login for IP: {ip}\n")
        ftp.quit()
    except Exception as e:
        if output_file is not None:
            output_file.write(f"Error connecting to {ip}: {str(e)}\n")

def process_ips(ip_list, output_file):
    for ip in ip_list:
        connect_ftp(ip, output_file)

def parse_arguments():
    parser = argparse.ArgumentParser(description='FTP Tool')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-l', '--list', metavar='ipList.txt', help='File containing list of IP addresses')
    group.add_argument('-d', '--single-ip', metavar='IP', help='Single IP address')
    parser.add_argument('-o', '--output', metavar='output.txt', type=str, help='Output file')
    args = parser.parse_args()

    if not args.list and not args.single_ip:
        # Read from stdin
        ip_list = sys.stdin.read().splitlines()
    elif args.list and not args.list.strip():
        parser.error('No input file provided with -l/--list')
    elif args.list:
        with open(args.list, 'r') as ip_file:
            ip_list = ip_file.read().splitlines()
    else:
        ip_list = [args.single_ip]

    return args, ip_list

def main():
    args, ip_list = parse_arguments()

    output_file = None
    if args.output:
        output_file = open(args.output, 'w')

    process_ips(ip_list, output_file)

    if output_file:
        output_file.close()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.argv.append('--help')
    main()

