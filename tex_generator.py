#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 15:57:59 2018

@author: sara-es

This script takes an input csv and image collection
and returns a latex formated text snippet which can be
used to populate a flashcard

"""

import csv
with open('cards.csv', newline='') as csvfile:
    creader = csv.reader(csvfile, delimiter=',')
    catalogue = open('latex/catalogue.tex', 'w')
    for row in creader:
        #sorry for the hardcoding hackjob
        name = row[2].title()
        img = row[2].replace(' ', '-').lower()
        carbon = row[1].split('.',1)[0]
        cals = row[3].split('.',1)[0]
        prot = row[4].split('.',1)[0]
        fib = row[5].split('.',1)[0]
        sugar = row[6].split('.',1)[0]
        fat = row[7].split('.',1)[0]
        catalogue.write('\card{{{}}}{{{}}}{{{}}}{{{}}}{{{}}}{{{}}}{{images/{}.png}}\n'.format(
            name, carbon, cals, fat, sugar, fib, img))
        
        #if I export data properly
        #print('\card{{{}}}{{{}}}{{{}}}{{{}}}{{{}}}{{{}}}'.format(row[i] for i in row[1:6], img)