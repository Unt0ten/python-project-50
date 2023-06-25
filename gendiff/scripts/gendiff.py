#!/usr/bin/env python3

from gendiff import generate_diff
from gendiff.cli import parser_args


def main():
    args = parser_args()
    print(
        generate_diff(args.first_file, args.second_file, formater=args.format))


if __name__ == '__main__':
    main()
