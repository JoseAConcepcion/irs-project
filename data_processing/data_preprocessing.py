"""
This file includes all the techniques applied for review cleaning. It outputs a cleaned dataset for further use.
"""
import pandas as pd
import os
import demoji
demoji.download_codes()
import spacy
nlp = spacy.load("en_core_web_sm")

class Process():
    def __init__(self, data):
        self.df = pd.DataFrame()
        self.df['Review_Text'] = data
    def lower(self):
        # This function is used for lowercasing all dataset before applying any feature extraction technique.
        self.df['processed'] = self.df['Review_Text'].str.lower()
    def demojify(self):
        # This function is used to remove all emoji from dataset before applying any feature extraction technique.
        for text in self.df['processed']:
            text = demoji.replace(str(text))