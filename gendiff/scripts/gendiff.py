#!/usr/bin/env python3

from gendiff import generate_diff
from gendiff.cli import parse_args


def main():
    '''Compares two configuration files and shows a difference'''
    parser = parse_args()
    print(
        generate_diff(parser.first_file, parser.second_file,
                      formater=parser.format))


if __name__ == '__main__':
    main()
