import cPickle as pkl
import sys

map = pkl.load(open('dict_youtube_mapping.pkl','rb'))
print map
for i,j in map.items():
    print j,i