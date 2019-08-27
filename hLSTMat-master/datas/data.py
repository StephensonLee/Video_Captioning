import numpy
import os
import cPickle


feat = numpy.load('vid1713.npy')
print feat
for i in range(1,1970,1):
    feat = numpy.load('D:/Lib/feature/vid'+str(i)+'.npy')
    print feat
