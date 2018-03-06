import spacy

nlp_en = spacy.load('en')

print(nlp_en.vocab.vectors_length)

doc_en = nlp_en("hello world")

for token in doc_en:
	print("{}: {}".format(token, token.vector[:5]))

nlp_pt = spacy.load('en')

print(nlp_pt.vocab.vectors_length)

doc_pt = nlp_pt("olá mundo")

for token in doc_pt:
	print("{}: {}".format(token, token.vector[:5]))
