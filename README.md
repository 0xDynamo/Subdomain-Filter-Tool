 Subdomain Filter
======================

This tool allows users to filter subdomain data given from various enumeration tools such as Amass or subl1ster for a given root domain from a file. It's handy when you're dealing with large amounts of data and you're interested only in specific subdomains.

Usage:
------
python filter_subdomains.py -i input_file -d root_domain [-o output_file] [-r off_scope]

## Features

- File Input: Specify an input file for the tool to process.
- Domain Filter: Provide a root domain to filter its subdomains from the input file.
- Output File: Optionally specify a file to write the filtered subdomains.
- Off-Scope Subdomains: Exclude specific subdomains that are out of the scope.
- IP Extraction: Extract and output sorted and uniqued IP addresses from the input file.
- IP Output File: Optionally specify a file to write the extracted IP addresses.



Arguments:
----------
- `-i <input_file>`: Specify the path to the input file containing subdomains.
- `-d <root_domain>`: Specify the root domain to filter subdomains.
- `-r <off_scope>`: Optional. Provide a wildcard or file with off-scope wildcards to exclude specific subdomains.
- `-o <output_file>`: Optional. Specify a file to write the filtered subdomains.
- `-ip`: Optional. Extract and output sorted and uniqued IP addresses from the input file.
- `-oI <output_ips_file>`: Optional. Specify a file to write the extracted IP addresses.


Examples:
---------
1. Filter subdomains from 'subdomains.txt' with root domain 'tesla.com' and print the results:
   ```python filter_subdomains.py -i subdomains.txt -d domain```

2. Filter subdomains from 'subdomains.txt' with root domain 'tesla.com' and write the results to 'filtered_subdomains.txt':
  ```python filter_subdomains.py -i subdomains.txt -d domain -o filtered_subdomains.txt```

3. Filter subdomains from 'subdomains.txt' with root domain 'tesla.com' and specify an off-scope wildcard pattern:
```python filter_subdomains.py -i subdomains.txt -d domain -r wildcard.subdomain.root```

4. Filter subdomains from 'subdomains.txt' with root domain 'tesla.com' and specify an off-scope wildcard file:
   ```python filter_subdomains.py -i subdomains.txt -d domain -r off_scope.txt```
   
5. Filter subdomains, exclude off-scope subdomains, and extract IP addresses:
   ```python filter_subdomains.py -i subdomains.txt -d example.com -r off-scope.txt -ip -oI extracted_ips.txt```
   
6. Extract IP addresses only:
   ```python filter_subdomains.py.py -i subdomains.txt -ip -oI extracted_ips.txt```

Note:
-----
- The tool matches subdomains based on the specified root domain and removes any subdomains that match the off-scope wildcard patterns.
- Off-scope wildcards should use the '*' character as a placeholder for subdomain parts. For example, 'wildcard.subdomain.root' will match 'chatbot.indeed.com', 'simplyhired.com', etc.
- The tool supports both file-based and single wildcard off-scope patterns. If the off-scope argument is a file path, it will read the wildcards from the file. If it is a single wildcard pattern, it will treat it as an off-scope pattern.
- Ensure that the specified input file, off-scope file (if provided), and output files are accessible and have appropriate write permissions.


## Installation

Clone this repository to your local system:

git clone https://github.com/YourUsername/subdomain-filter.git

**Ensure you have Python 3 installed on your system.**

cd subdomain-filter

```python3 filter_subdomains.py ...```



## License

[MIT](https://choosealicense.com/licenses/mit/)
