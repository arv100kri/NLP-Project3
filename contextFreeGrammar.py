'''
Created on Feb 28, 2013

@author: koolkid
'''
DEV_FILE = "twpos-data-v0.3/oct27.splits/oct27.dev"
GENERATED_FILES = "generated_files/"

import parseTwitter
'''
def getTweet(fileName):
    f = open(GENERATED_FILES+"tweets", 'w')
    words = []
    tags = []
    with open(fileName) as twitter_file:
        for line in twitter_file:
            if len(line) > 1:
                lister = line.split("\t")
                words.append(lister[0].rstrip())
                tags.append(lister[1].rstrip())
            else:
                if len(words) <10:
                    for word in words:
                        f.write(word + " ")
                    f.write("\t[")
                    for tag in tags:
                        f.write(tag + " ")
                    f.write("]\n")
                words = []
                tags = []
    f.close()

getTweet(DEV_FILE)
'''
'''
output = parseTwitter.evalParser("file:jagannathan-task2.cfg", DEV_FILE, True)
print output
'''
output = parseTwitter.evalParser("file:jagannathan-task3.cfg", DEV_FILE, True, preprocessor=parseTwitter.preprocess)
print output