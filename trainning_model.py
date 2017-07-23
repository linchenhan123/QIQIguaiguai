import numpy as np
import cv2

samples = np.load('/home/lin/samples.npy')
labels = np.load('label.npy')

k = 70
train_label = labels[10:k]
train_input = samples[10:k]
test_input = samples[:10]
test_label = labels[:10]

model = cv2.ml.KNearest_create()
model.train(train_input,cv2.ml.ROW_SAMPLE,train_label)

retval , results , neigh_resp, dists = model.findNearest(test_input,1)
string = results.ravel()

print(test_label.reshape(1,len(test_label))[0])
print(string)
