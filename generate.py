from lib.util import start_string, end_string, description_text
from sys import argv, exit
from argparse import ArgumentParser

def make_string(i: int) -> str:
    """
    Returns a string based on the input number.

    Parameters:
    i (int): The input number.

    Returns:
    str: The generated string.
    """
    result = " {\n\t\tprintln!(\"Even.\");\n\t\t()\n\t}\n"
    if i % 2 != 0:
        return " {\n\t\tprintln!(\"Odd.\");\n\t\t()\n\t}\n"
    
    return result

def main():
    # Parse arguments
    parser = ArgumentParser(description=description_text)
    parser.add_argument('-o', '--output', type=str, default='parity.rs', 
                        help='output file path')
    parser.add_argument('-r', '--range', type=str, default='u16', 
                        choices=['u8', 'u16', 'u32', 'u64'], 
                        help='desired integer length')
    args = parser.parse_args()

    # Choose integer precision
    option = args.range
    Ranges = { # Dictionary of ranges
        "u8": range(0, 2**8),
        "u16": range(0, 2**16), # default
        "u32": range(0, 2**32),
        "u64": range(0, 2**64)
    }

    # Write to file
    try:
        with open(args.output, 'w') as file:
            file.write(start_string)
            # Brilliant metaprogramming goes here
            for i in Ranges[option]:
                file.write(f"\tif number == {i}")
                file.write(make_string(i))

            file.write(end_string)
        print("File written successfully.")
    except IOError:
        print("Error: Unable to write to file.")

    exit(0) # No idea why 


if __name__ == "__main__":
    main()