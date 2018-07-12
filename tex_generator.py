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
        #Hardcoding hackjob
        #Data should be in .csv format columns name, caption, time in car, carbon, kcals, fat, sugar, protein, img filename
        name = row[0]
        subcap = row[1]
        carTime = row[2]
        img = row[8]
        carbon = row[3]
        cals = row[4]
        prot = row[7]
        sugar = row[6]
        fat = row[5]
        catalogue.write('\card{{{}}}{{{}}}{{{}}}{{{}}}{{{}}}{{{}}}{{{}}}{{{}}}{{images/{}}}\n'.format(
            name, subcap, carTime, carbon, cals, fat, sugar, prot, img))        

