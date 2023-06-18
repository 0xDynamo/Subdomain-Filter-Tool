 Subdomain Filter Tool
======================

This tool allows users to filter subdomain data given from various enumeration tools such as Amass or subl1ster for a given root domain from a file. It's handy when you're dealing with large amounts of data and you're interested only in specific subdomains.

Usage:
------
python filter_subdomains.py -i input_file -d root_domain [-o output_file] [-r off_scope]

Arguments:
----------
  -i, --input    : Input file path containing the list of subdomains.
  -d, --domain   : Root domain to filter the subdomains.
  -o, --output   : Optional. Output file to write the filtered subdomains. If not specified, results will be printed to the console.
  -r, --off-scope: Optional. Wildcard or file containing off-scope wildcards. Wildcards should use the '*' character as a placeholder for subdomain parts.

Examples:
---------
1. Filter subdomains from 'subdomains.txt' with root domain 'tesla.com' and print the results:
   python filter_subdomains.py -i subdomains.txt -d domain

2. Filter subdomains from 'subdomains.txt' with root domain 'tesla.com' and write the results to 'filtered_subdomains.txt':
   python filter_subdomains.py -i subdomains.txt -d domain -o filtered_subdomains.txt

3. Filter subdomains from 'subdomains.txt' with root domain 'tesla.com' and specify an off-scope wildcard pattern:
   python filter_subdomains.py -i subdomains.txt -d domain -r wildcard.subdomain.root

4. Filter subdomains from 'subdomains.txt' with root domain 'tesla.com' and specify an off-scope wildcard file:
   python filter_subdomains.py -i subdomains.txt -d domain -r off_scope.txt

Note:
-----
- The tool matches subdomains based on the specified root domain and removes any subdomains that match the off-scope wildcard patterns.
- Off-scope wildcards should use the '*' character as a placeholder for subdomain parts. For example, 'wildcard.subdomain.root' will match 'chatbot.indeed.com', 'simplyhired.com', etc.
- The tool supports both file-based and single wildcard off-scope patterns. If the off-scope argument is a file path, it will read the wildcards from the file. If it is a single wildcard pattern, it will treat it as an off-scope pattern.



## License

[MIT](https://choosealicense.com/licenses/mit/)
