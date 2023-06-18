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

def main():
    parser = argparse.ArgumentParser(description='Filter subdomains from file')
    parser.add_argument('-i', metavar='input', type=str, required=True, help='Input file path')
    parser.add_argument('-d', metavar='domain', type=str, required=True, help='Root domain to filter subdomains')
    parser.add_argument('-o', metavar='output', type=str, help='Output file to write the result')
    parser.add_argument('-r', '--off-scope', type=str, help='Wildcard or file containing off-scope wildcards')
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
        print(f'Output has been written to {args.o}')
    else:
        print('\n'.join(subdomains))

if __name__ == "__main__":
    main()
