# Subdomain Filter Tool

This tool allows users to filter subdomains for a given root domain from a file. It's handy when you're dealing with large amounts of data and you're interested only in specific subdomains.

## Features

- **File Input**: You can specify a file for the tool to process.
- **Domain Filter**: You can specify a root domain to filter out its subdomains from the given file.
- **Output File**: You can specify a file where the filtered subdomains will be written.

## Installation

Clone this repository into your local system.


git clone https://github.com/YourUsername/subdomain-filter.git


Move into the cloned repository.


cd subdomain-filter


## Usage

To use the tool, you need to provide it with a file and a root domain. You can also specify an output file.

### Syntax


python subdomain_filter.py -f <file> -d <domain> [-o <output>]


### Parameters

- `-f <file>`: This parameter is used to specify the file to be processed. Replace `<file>` with the path of the file.
- `-d <domain>`: This parameter is used to specify the root domain. Replace `<domain>` with the root domain (for example, 'indeed' or 'indeed.com').
- `-o <output>`: This is an optional parameter used to specify the output file. If not provided, the output will be printed on the console. Replace `<output>` with the path of the output file.

## Examples


python subdomain_filter.py -f myfile.txt -d indeed.com


This command will process 'myfile.txt' and filter out subdomains of 'indeed.com', printing the results on the console.


python subdomain_filter.py -f myfile.txt -d indeed.com -o output.txt


This command will process 'myfile.txt', filter out subdomains of 'indeed.com', and write the results to 'output.txt'.

## License

[MIT](https://choosealicense.com/licenses/mit/)
