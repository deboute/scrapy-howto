# -*- coding: utf-8 -*-
# -*- python -*-
# use 4 spaces to indent, NO TAB
# vim: ai ts=4 sts=4 et sw=4
"""
Generate a set of common words based on files present in the current folder
"""
#
# IMPORTS
#
# BASE
import os
import glob

common_words = set()
words_dir = os.path.dirname(__file__)

# build a list of normalized common words to ignore
for words_file in glob.glob(os.path.join(words_dir, '*.txt')):
    with open(
        os.path.join(
            words_dir,
            words_file
        ),
        'r'
    ) as fh:
        for line in fh:
            common_words.add(
                unicode(line.strip().lower())
            )

