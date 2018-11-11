credits to [mark Jay](https://github.com/markjay4k/Install-Tensorflow-on-Ubuntu-17.10-/blob/master/Tensorflow%20Install%20instructions.ipynb)

and [his youtube](https://www.youtube.com/watch?v=vxjbL5iN1XY)

## update GPU driver, this one should be more than 390
```
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
sudo apt install nvidia-390
```
to verify by using ```nvidia-smi```

## install cuda version 9.0 (with all patches)
go to [cuda](https://developer.nvidia.com/cuda-90-download-archive) and download the toolkit for linux, x86_64, ubuntu, 16.04, deb
```
sudo dpkg -i cuda-repo-ubuntu1704-9-0-local_9.0.176-1_amd64.deb
sudo apt-key add /var/cuda-repo-9-0-local/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda
(to download a specific version of cuda: sudo apt-get install cuda=9.0.176-1.)(from https://developer.nvidia.com/rdp/cudnn-archive)
```

## update path variable
put these in .bashrc
```
export PATH=/usr/local/cuda-9.0/bin${PATH:+:$PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

## install cudnn 7.0.5
go to https://developer.nvidia.com/cudnn

Select CUDNN 7.0.5 for CUDA 9.0

download the cuDNN v7.0.5 Library for Linux (tar file)

tar -xzvf cudnn-9.0-linux-x64-v7.tgz

run the following commands to move the appropriate files to the CUDA folder
```
sudo cp cuda/include/cudnn.h /usr/local/cuda/include
sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*
```
## install tensorflow gpu with pip
```
conda create -n tf python=3.6 pip
source activate tf
pip install tensorflow-gpu==1.5
```

### see tensorflow support version
![cuda support version](https://github.com/Emrys-Hong/machine_learning/blob/master/utils/tensorflow/tensorflow_support_version.png)


## test
```python
>>> import tensorflow as tf
>>> hello = tf.constant('hello tensorflow')
>>> with tf.Session() as sesh:
>>>     sesh.run(hello)
```
