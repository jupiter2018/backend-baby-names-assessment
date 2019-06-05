#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import argparse
import os

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here+++
    if not os.path.isfile(filename):
        print('This file does not exist. Try again')
        sys.exit(1)
    infolist = []
    namesdict = {}
    with open(filename,'r') as f:
        
        for line in f:
            #print(line)
            searchyear = re.search('Popularity\sin\s(\d{4})',line)
            #print('hello',searchobject)
            if searchyear:
                # print(searchyear.group(1))
                infolist.append(searchyear.group(1))
            searchnames = re.search('<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',line)
            if searchnames:
                # print(searchnames.group(1))
                # print(searchnames.group(2))
                # print(searchnames.group(3))
                namesdict[searchnames.group(2)]= searchnames.group(1)
                namesdict[searchnames.group(3)]= searchnames.group(1)

    for name in sorted(namesdict.keys()):
        infolist.append(name+ ' '+ namesdict[name])
    #print(infolist)
    return infolist
    


def create_parser():
    """Create a cmd line parser object with 2 argument definitions"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more filenames.
    # It will also expand wildcards just like the shell, e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1)

    file_list = args.files

    # option flag
    create_summary = args.summaryfile

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    for file in file_list:
        if(not file == 'files'):
            mylist = extract_names(file)
            text = '\n'.join(mylist) + '\n'
            if(create_summary):
                with open(file+'.summary','a') as filetowrite:
                    filetowrite.write(text)
            else:
                print(text)

    # or write it to a summary file


if __name__ == '__main__':
    main()
