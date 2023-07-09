
FTPNinja is a powerful tool for automating FTP login attempts and checking the success of login without credentials. It provides a convenient way to test and validate FTP login  for multiple IP addresses.

## Installation

1. Clone the repository:
   ```
   git clone <repository_url>
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Obtain a Shodan API key by signing up for a Shodan membership at [https://www.shodan.io](https://www.shodan.io). The Shodan membership is required to retrieve information about IP addresses, which can be useful for selecting potential FTP targets.

## Usage

FTPNinja supports multiple ways to provide IP addresses for FTP login attempts. Choose the method that suits your needs:

### Method 1: List of IP addresses

1. Prepare a text file (`ipList.txt`) containing a list of IP addresses, with each IP address on a separate line.

2. Run FTPNinja with the list file:
   ```
   python3 ftpNinja.py -l ipList.txt -o output.txt
   ```
   Replace `ipList.txt` with the path to your IP address list file, and `output.txt` with the desired output file name.

### Method 2: Single IP address

1. Run FTPNinja with a single IP address:
   ```
   python3 ftpNinja.py -d 192.168.1.1 -o output.txt
   ```
   Replace `192.168.1.1` with the IP address you want to test, and `output.txt` with the desired output file name.

### Method 3: Piped input

1. To use piped input, provide the IP addresses through stdin using the `cat` command or any other method:
   ```
   cat ipList.txt | python3 ftpNinja.py -o output.txt
   ```
   Replace `ipList.txt` with the path to your IP address list file, and `output.txt` with the desired output file name.

**Note:** The Shodan API key is required to retrieve information about IP addresses. Make sure to set the `SHODAN_API_KEY` environment variable to your Shodan API key before running the tool.

## Output

FTPNinja will perform FTP login attempts for the provided IP addresses and display the success messages. If an output file is specified, the success messages will be saved to the file.
