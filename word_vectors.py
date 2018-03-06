import spacy

# English
print('English')
nlp_en = spacy.load('en')

doc_en = nlp_en('cat')

aux_list_en = [nlp_en('can'), nlp_en('dog')]

for i in aux_list_en:
	print("Similarity between {} and {}: {}".format(doc_en, i, doc_en.similarity(i)))


# Portuguese
print('Português')
nlp_pt = spacy.load('en')

doc_pt = nlp_pt("gato")

aux_list_pt = [nlp_pt('fato'), nlp_pt('cachorro')]

for i in aux_list_pt:
	print("Similaridade entre {} e {}: {}".format(doc_pt, i, doc_pt.similarity(i)))
