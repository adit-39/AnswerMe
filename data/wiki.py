import wikipedia

def getpage(name):
	pg = wikipedia.page(name)
	print "getting page"
	with open(name+".txt","w") as f:
		f.write(pg.content.encode("ascii","ignore"))
	with open("union.txt","a") as f:
		f.write(pg.content.encode("ascii","ignore"))
	return pg.url,pg.title,pg.content


def get_data():
	with open("topics.txt") as f:
		topics = f.readlines();
		return topics



topics = get_data()
for item in topics:
	url,title, content = getpage(item.strip())
	print "Url :"+ url +"\nTitle : "+title+"\n"
