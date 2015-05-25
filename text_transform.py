import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.lancaster import LancasterStemmer
import operator

def text_translate(filename='Gandhi.txt', stem=True):
	f = open(filename,"r")
	text = f.read()
	f.close()
	re_tokenizer = RegexpTokenizer('[A-Z]\w+')
	words = re_tokenizer.tokenize(text)
	#print words
	st = LancasterStemmer()
	if(stem):
		stemmed=[]
		for i in words:
			stemmed.append(st.stem(i.lower()))
		return stemmed
	else:
		return words

def find_unigram_dist(voc,stemmed):
	tot = len(stemmed)
	freq_voc=[]
	for i in voc:
		freq_voc.append((i[0],i[1]/float(tot)))
	return freq_voc

def derive_vocabulary(stemmed,num):
	fd = nltk.FreqDist(stemmed)
	sorted_fd = sorted(fd.items(), key = operator.itemgetter(1))
	voc = sorted_fd[num*-1:]
	voc_dist = find_unigram_dist(voc,stemmed)
	return voc,voc_dist
	
if __name__=='__main__':
	#text_translate()
	stemmed = text_translate(stem=False)
	#print stemmed_voc
	voc, voc_dist = derive_vocabulary(stemmed,100)
	print voc_dist
	#f = open("stemmed","w")
	#f.write()
