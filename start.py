import pymongo
import igraph
from pymongo import MongoClient
from igraph import *

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.local

c=db.followers.find();
l=[];
g=Graph();
for i in range(0,10000):
	 #print c[i]['login'],c[i]['follows']
	 if(c[i]['login'] not in l):
	 	l.append(c[i]['login'])
	 	g.add_vertex();
	 	n1=len(l)-1;
	 else:
	 	n1=l.index(c[i]['login']);

	 if(c[i]['follows'] not in l):
	 	l.append(c[i]['follows'])
	 	g.add_vertex();
	 	n2=len(l)-1;
	 else:
	 	n2=l.index(c[i]['follows']);
	 g.add_edges([(n1,n2)]);

g.vs["label"] =l;
#g.vs["color"]="rgb(0, 127, 255)";
#g.vs["size"]=1
#print g;
plot(g)






