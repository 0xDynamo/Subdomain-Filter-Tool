Subdomain Filter Tool
The Subdomain Filter Tool is a Python script designed to extract specific subdomains from a file or text. It can be very useful when you want to analyze only a particular set of subdomains from a larger data set.

Installation
To use this tool, you will need Python 3.6 or later. You can check your Python version with python3 --version. If you have the correct Python version, you can clone this repository and run the script.

Usage
You can use this tool by running the following command in your terminal:

bash
Copy code
python3 subdomain_filter.py -f [FILENAME] -d [DOMAIN]
In this command:

[FILENAME] should be replaced with the name of the file you want to analyze. The tool will read this file and find all the subdomains of the domain you specify.
[DOMAIN] should be replaced with the domain you're interested in. The tool will find all subdomains of this domain in the file you provide.
Example usage:

bash
Copy code
python3 subdomain_filter.py -f my_file.txt -d indeed.com
This command will read my_file.txt and print all subdomains of indeed.com found in the file.

Output to a File
If you want the result to be written to a file instead of printed to the console, you can use the -o flag followed by the output file name:

bash
Copy code
python3 subdomain_filter.py -f my_file.txt -d indeed.com -o output.txt
This command will write the subdomains found to output.txt.

Disclaimer
This tool is provided as is, without any warranty. It's intended for educational purposes and should not be used for malicious activities.