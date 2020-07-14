# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:15:45 2019

@author: 17069455
"""

class TextFrequency():
    def __init__(self,file_name):
        self.file_name=file_name
        self.text=[]
        self.getText()
        self.letterFreq()
        self.wordFreq()
        
    def getText(self):
        txt_file=open(self.file_name,'r')
        self.text=txt_file.read()
        self.text=self.text.split('\n')
        self.text=(' ').join(self.text)
        txt_file.close()
        
    def letterFreq(self):
        freq={}
        for letter in self.text:
            if letter in freq:
                freq[letter]=freq[letter]+1
            else:
                freq[letter]=1
        return freq
            
    def wordFreq(self):
        freq={}
        words=(self.text).split(' ')
        for word in words:
            if word in freq:
                freq[word]=freq[word]+1
            else:
                freq[word]=1
        return freq
    
    def toLower(self):
        self.text=self.text.lower()

class HistogramPrinter(TextFrequency):
    def __init__(self,file_name):
        TextFrequency.__init__(self,file_name)
    
    def printLetterHist(self):
        freq={}
        freq=self.letterFreq()
        for item in freq:
            asterix=""
            while len(asterix)< freq[item]:
                asterix=asterix+'*'
            print(item,asterix)
    
    def printWordHist(self):
        freq={}
        freq=self.wordFreq()
        for item in freq:
            asterix=""
            while len(asterix)<freq[item]:
                asterix=asterix+'*'
            print(item,asterix)
            
#myTextFrequency=TextFrequency('lyrics.txt')

#letterFreq=myTextFrequency.letterFreq()
#for letter in letterFreq:
 #   print(letter,letterFreq[letter])

#wordFreq=myTextFrequency.wordFreq()
#for word in wordFreq:
    #print(word,wordFreq[word])

myHistogram=HistogramPrinter('lyrics.txt')
myHistogram.printLetterHist()
#myHistogram.printWordHist()

#myHistogram.toLower()
#myHistogram.printWordHist()
#myHistogram.printLetterHist()