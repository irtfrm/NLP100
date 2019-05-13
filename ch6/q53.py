import xml.etree.ElementTree as ET

with open('nlp.txt.xml', 'r') as f:
    lines = ''.join(f.readlines()) 
root = ET.fromstring(lines)

sentences = root[0][1]
for sentence in sentences:
    for token in sentence[0]:
        print(token[0].text)

# [ Stanford Core NLPの使い方 ]
# Javaのバージョンが9以降だと'--add-modules java.se.ee'を付ける必要がある。
# java -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLP -file nlp.txt --add-modules java.se.ee