import nltk

def text_translate(file):
	with open(file,"r") as f:
		text=f.read()
		words = nltk.word_tokenise(text)
		#print words
		st = lancasterStemmer()
		stemmed =[]
		for i in words:
			stemmed.append(st.stem(i.lower()))
		return stemmed

stemmed_voc = text_translate("/pages/Gandhi")
print stemmed