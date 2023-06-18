import argparse
import re
import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f'File {file_path} not found.')
        return []

def filter_subdomains(file_content, root_domain, off_scope_list):
    # Match any subdomain of the root domain
    pattern = r'\b((?:[\w-]+\.)?' + re.escape(root_domain) + r')\b'
    matches = re.findall(pattern, ' '.join(file_content))

    # Construct patterns for each wildcard in off-scope list
    off_scope_patterns = [re.escape(item).replace(r'\*', '[\w-]+') for item in off_scope_list]

    # Add also patterns without wildcards (e.g., conv.indeed.com)
    off_scope_patterns += [re.escape(item.replace('*.', '')) for item in off_scope_list]

    # Remove matches that fit any off-scope pattern
    for off_scope_pattern in off_scope_patterns:
        matches = [match for match in matches if not re.fullmatch(off_scope_pattern, match)]
        
    return matches

def extract_ips(file_content):
    # Match IP addresses using regex
    pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    matches = re.findall(pattern, ' '.join(file_content))
    unique_ips = list(set(matches))
    sorted_ips = sorted(unique_ips)
    
    return sorted_ips

def main():
    parser = argparse.ArgumentParser(description='Filter subdomains from file and extract IP addresses')
    parser.add_argument('-i', metavar='input', type=str, required=True, help='Input file path')
    parser.add_argument('-d', metavar='domain', type=str, required=True, help='Root domain to filter subdomains')
    parser.add_argument('-o', metavar='output', type=str, help='Output file to write the filtered subdomains')
    parser.add_argument('-r', '--off-scope', type=str, help='Wildcard or file containing off-scope wildcards')
    parser.add_argument('-ip', action='store_true', help='Extract IP addresses from the input file')
    parser.add_argument('-oI', metavar='output_ips', type=str, help='Output file to write the extracted IP addresses')
    args = parser.parse_args()

    file_content = read_file(args.i)
    
    # Load off-scope list from file or as a single wildcard from argument
    if args.off_scope:
        if os.path.isfile(args.off_scope):
            off_scope_list = read_file(args.off_scope)
        else:
            off_scope_list = [args.off_scope]
    else:
        off_scope_list = []

    subdomains = filter_subdomains(file_content, args.d, off_scope_list)

    if args.o:
        with open(args.o, 'w') as output_file:
            for subdomain in subdomains:
                output_file.write(f'{subdomain}\n')
        print(f'Filtered subdomains have been written to {args.o}')
    else:
        print('\n'.join(subdomains))

    if args.ip:
        ips = extract_ips(file_content)
        if args.oI:
            with open(args.oI, 'w') as output_ips_file:
                for ip in ips:
                    output_ips_file.write(f'{ip}\n')
            print(f'Extracted and sorted IP addresses have been written to {args.oI}')
        else:
            print('\n'.join(ips))

if __name__ == "__main__":
    main()
