# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 21:12:57 2015

@author: Ashish Yadav
"""

input_file = open('sents_train_lc_nopunc.txt', 'r')
file_contents = input_file.read()
input_file.close()
word_list = file_contents.split()

out_file = open('vocabulary.txt', 'w')

unique_words = set(word_list)
for word in unique_words:
    if(not(word[:3]=="vid" and word[3:].isdigit())):
        out_file.write(str(word) + "\n")
out_file.close()