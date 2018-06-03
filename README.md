# dogCNN
unimelb project
This is a simple program that use Caffe to train a dog recognization CNN.
# install Caffe
https://github.com/BVLC/caffe follow the instruction to install Caffe. Move Caffe folder to this folder or change the path in bat file according to your own environment.
# prepare data
Prepare your training dataset and split them into two set (one for train and one for evaluate). Put two datasets into train folder and val folder. Generate two text files listing all the file name of the pictures and their labels (follow my templates).

Run convert_trainset.bat and convert_valset.bat files to covert picture to lmdb format.
Run computeMean.bat file to generate meanfile.
# adjust model
In train_val.prototxt file change the output of last layer (line 373) to fit you data.
You can also adjust the hyperparameter in solver.protetxt file to make you model perform better (not necessary).

# train model
Run caffe_train.bat file to train the model.
fine-tuning: download pretrained model http://dl.caffe.berkeleyvision.org/bvlc_reference_caffenet.caffemodel
	Run caffe_continue.bat to train model by using pretrained model as initialized weight.
  
# transform to IOS
write a file listing names for all classes (label.txt).
change deploy.prototxt as same as train_val.prototxt.
copy .caffemodel, deploy.prototxt, mean file, label.txt and coremltool.py to a Mac computer and Run coremltool.py (maybe need to change some configuration) to generate a mlmodel file. Now we can use this file in IOS project directly.
