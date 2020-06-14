#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Ruth Mayodi, ruthmayodi with the help of Howard Post "


import sys
import argparse

def text_upper(text):
    """ Returns uppercase text """
    return text.upper()

def text_lower(text):
    """ Returns lowercase text """
    return text.lower()

def text_title(text):
    """ Returns titlecase text """
    return text.title()


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser1 = argparse.ArgumentParser(
        description = "Perform transformation on input text.")
    parser1.add_argument(
        '-u', '--upper', 
        help= 'convert text to uppercase', 
        action = 'store_true'
    )
    parser1.add_argument(
        '-l', '--lower',
        help = 'convert text to lowercase', 
        action = 'store_true'
    )
    parser1.add_argument(
        '-t', '--title',
        help = 'convert text to titlecase',
        action = 'store_true'
    )
    parser1.add_argument(
        'text', help = 'text to be manipulated'
    )
    return parser1


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    ns = parser.parse_args(args)
    if not ns:
        parser.print_help()
        exit(1)
    text = ns.text
    if ns.upper:
        text = text_upper(text)
    if ns.lower:
        text = text_lower(text)
    if ns.title:
        text = text_title(text)
    print(text)

    return


if __name__ == '__main__':
    main(sys.argv[1:])
