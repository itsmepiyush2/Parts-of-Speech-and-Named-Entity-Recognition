import spacy
sp = spacy.load('en_core_web_sm')

input_sentence = input("Enter a sentence: ")
sentence = sp(input_sentence)
for entity in sentence.ents:
	print(entity.text + ' - ' + entity.label_ + ' - ' + str(spacy.explain(entity.label_)))

from spacy import displacy
displacy.serve(sentence, style = 'ent')