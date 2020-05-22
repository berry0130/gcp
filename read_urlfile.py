import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0
print(train_images.shape)
import numpy as np 
# train_images=np.delete(train_images,1, axis=0)
# print(train_images.shape)
# train_images=np.delete(np.delete(np.delete(train_images[0], np.s_[::1], axis=0),np.s_[::1], axis=1),np.s_[::1], axis=2)

# print(train_images.shape)
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']
# print('label')
# print(train_labels[0][0])
# print(train_labels[19][0])
# print(train_labels[23][0])
# print(train_labels[22][0])
# print('end')
# train_images=np.delete(np.delete(np.delete(np.delete(train_images, np.s_[::1], axis=3),np.s_[::1],axis=0),np.s_[::1],axis=2),np.s_[::1],axis=1)
# train_deer_image = np.zeros((0,32,32,3))
# train_deer_label = np.zeros((5000,1))
train_deer_image = np.empty((5000,32,32,3))
train_deer_label = np.empty((5000,1))
train_hourse_image = np.empty((5000,32,32,3))
train_hourse_label = np.empty((5000,1))
test_image_use_t = np.empty((5000,32,32,3))
test_label_use_t = np.empty((5000,1))
# print(train_images.shape)
k=0
j=0
train_image_use = np.empty((519+486,32,32,3))
train_label_use = np.empty((519+486,1))
for i in range(519+486):
  if train_labels[i][0] == 4:
    # train_images=np.delete(train_images,i, axis=0)
    # train_labels=np.delete(train_labels,i, axis=0)
    # np.concatenate((train_cat[i], train_images[i]))
    # np.concatenate((train_deer_image,np.resize(train_images[i],(0,32,32,3))), axis=0)
      # np.append(train_deer_image[k],train_images[i],axis=0)
      # train_deer_image[k]=train_images[i]
      # train_deer_label[k]=train_labels[i][0]
    train_image_use[k]=train_images[i]
    # train_deer_label[k]=train_labels[i][0]
    train_label_use[k]=0
  if train_labels[i][0] == 7:
    train_image_use[k]=train_images[i]
    # train_hourse_label[j]=train_labels[i][0]
    train_label_use[k]=1
plt.figure(figsize=(10,10))
for i in range(100):
    plt.subplot(10,10,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_deer_image[i], cmap=plt.cm.binary)
    # The CIFAR labels happen to be arrays, 
    # which is why you need the extra index
    plt.xlabel(class_names[int(train_deer_label[i])])
plt.show() 

for i in range(1000):
  if test_labels[i][0] == 4:
    test_image_use_t[j]=test_images[i]
    test_label_use_t[j]=0
    j=j+1
  if test_labels[i][0] == 7:
    test_image_use_t[j]=test_images[i]
    test_label_use_t[j]=1
    j=j+1
print(j)
test_image_use = np.empty((192,32,32,3))
test_label_use = np.empty((192,1))
for i in range(191):
  test_image_use[i]=test_image_use_t[i]
  test_label_use[i]=test_label_use_t[i]
  plt.xticks([])
  plt.yticks([])
  plt.grid(False)
  plt.imshow(test_image_use[i], cmap=plt.cm.binary)
  plt.xlabel(test_label_use[i])
  plt.show() 