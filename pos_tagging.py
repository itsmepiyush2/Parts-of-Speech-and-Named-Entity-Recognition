import spacy
sp = spacy.load('en_core_web_sm')

input_sentence = input("Enter a sentence: ")
sentence = sp(input_sentence)

print(sentence.text)

for word in sentence:  
    print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')

from spacy import displacy
displacy.serve(sentence, style = 'dep',options = {'distance': 85})