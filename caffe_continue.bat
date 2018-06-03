SET GLOG_logtostderr=1  
.\caffe\build\tools\Release\caffe.exe train --solver=solver.prototxt --weights=bvlc_reference_caffenet.caffemodel
pause