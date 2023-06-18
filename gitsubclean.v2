import argparse
import re

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f'File {file_path} not found.')
        return ''

def filter_subdomains(file_content, root_domain):
    # Match any subdomain of the root domain
    pattern = r'\b((?:[\w-]+\.)+' + re.escape(root_domain) + r')\b'
    matches = re.findall(pattern, file_content)
    return matches

def main():
    parser = argparse.ArgumentParser(description='Filter subdomains from file')
    parser.add_argument('-i', metavar='input', type=str, required=True, help='Input file path')
    parser.add_argument('-d', metavar='domain', type=str, required=True, help='Root domain to filter subdomains')
    parser.add_argument('-o', metavar='output', type=str, help='Output file to write the result')
    args = parser.parse_args()

    file_content = read_file(args.i)
    subdomains = filter_subdomains(file_content, args.d)

    if args.o:
        with open(args.o, 'w') as output_file:
            for subdomain in subdomains:
                output_file.write(f'{subdomain}\n')
        print(f'Output has been written to {args.o}')
    else:
        print('\n'.join(subdomains))

if __name__ == "__main__":
    main()
