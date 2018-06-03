import coremltools
model = coremltools.converters.caffe.convert('caffe_alexnet_train_iter_4500.caffemodel', \
	'deploy.prototxt', \
	'mimg_mean.binaryproto'), \
	image_input_names='data', is_bgr=True, class_labels = 'label.txt' )
model.save('dogmodel.mlmodel')