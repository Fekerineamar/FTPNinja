![FNinjalgo](https://github.com/Fekerineamar/Fekerineamar/blob/master/img/FNINJA.png)

FTPNinja is a powerful tool for automating FTP login attempts and checking the success of login without credentials. It provides a convenient way to test and validate FTP login for multiple IP addresses.

## Key Features
* FTP Connection: FTP Ninja allows users to establish FTP connections with remote servers.

* IP Validation: The tool validates the provided IP addresses to ensure they are valid and properly formatted.

* FTP Server Validation: FTP Ninja checks if the provided IP address corresponds to a valid FTP server.

* Login Authentication: FTP Ninja supports login operations to authenticate with the FTP server.

* Status Reporting: The tool provides detailed status reports for successful logins, login failures, and connection errors.

* Output Logging: FTP Ninja allows users to specify an output file to log successful login attempts.

* Command-line Interface: FTP Ninja has a command-line interface that supports different command-line options for specifying IP addresses, IP lists, and output files.

* Help Documentation: The tool includes a help message that provides information on how to use the command-line options.

These features make FTP Ninja a versatile tool for managing FTP connections, validating IP addresses, and performing FTP operations.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Fekerineamar/FTPNinja.git
   ```

2. Change To Directory:
   ```
   cd FTPNinja
   ```

## Usage

FTPNinja supports multiple ways to provide IP addresses for FTP login attempts. Choose the method that suits your needs:

```
usage: ftpNinja.py [-h] [-l ipList.txt] [-ip IP] [-w wordlist.txt] [-o output.txt]

FTP Tool

optional arguments:
  -h, --help            show this help message and exit
  -l ipList.txt, --list ipList.txt
                        File containing a list of IP addresses
  -ip IP, --single-ip IP
                        Single IP address
  -w wordlist.txt, --wordlist wordlist.txt
                        File containing usernames and passwords separated by ":"
  -o output.txt, --output output.txt
                        Output file

```

### Method 1: List of IP addresses
* Note: Use Python 3.7+

1. Prepare a text file (`ipList.txt`) containing a list of IP addresses, with each IP address on a separate line.

2. Run FTPNinja with the list file:
   ```
   python3 ftpNinja.py -l ipList.txt -o output.txt
   ```
   Replace `ipList.txt` with the path to your IP address list file, and `output.txt` with the desired output file name.

### Method 2: Single IP address

1. Run FTPNinja with a single IP address:
   ```
   python3 ftpNinja.py -ip 192.168.1.1 -o output.txt
   ```
   Replace `192.168.1.1` with the IP address you want to test, and `output.txt` with the desired output file name.

### Method 3: Piped input

1. To use piped input, provide the IP addresses through stdin using the `cat` command or any other method:
   ```
   cat ipList.txt | python3 ftpNinja.py -o output.txt
   ```
   Replace `ipList.txt` with the path to your IP address list file, and `output.txt` with the desired output file name.

### Brute Forcing:

1. Run FTPNinja with a -w wordlist:
   ```
   python3 ftpNinja.py -ip 192.168.1.1 -w wordlist.txt
   ```
   
## Example 
   ```
   cat ipList.txt | python3 ftpNinja.py 
   ```
   ![example](https://github.com/Fekerineamar/Fekerineamar/blob/master/img/e.g.png)
   ![example](https://github.com/Fekerineamar/Fekerineamar/blob/master/img/Fwget.png)
   
## Output

FTPNinja will perform FTP login attempts for the provided IP addresses and display the success messages. If an output file is specified, the success messages will be saved to the file.

- Happy Hacking ☠

- ツ Don't Forget To Follow Me ツ
<br>

[![facebook](https://img.shields.io/badge/-Facebook-1877F2?style=for-the-badge&logo=Figma&logoColor=eeffff)](https://www.facebook.com/profile.php?id=100076323828870)
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=eeffff)](https://github.com/FekerineAmar/)
[![Website](https://img.shields.io/badge/-Website-181717?style=for-the-badge&logo=Internet-Archive&logoColor=eeffff)](https://developer.x10.mx/)
