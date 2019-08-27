import cPickle as pkl
import sys
# vid = sys.argv[1]
vid = '1000'
print vid
cap = pkl.load(open('CAP.pkl','rb'))
#vid = '1849'
c = cap['vid'+vid]
for i in c:
    print i
    # print i['caption']

